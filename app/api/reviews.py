from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, Review
from app.forms import ReviewForm, validation_errors_formatter
from sqlalchemy.exc import IntegrityError


bp = Blueprint("reviews", __name__, url_prefix="/reviews")


@bp.route("/<int:review_id>", methods=["GET"])
def get_review(review_id):
    review = Review.query.get(review_id)
    if not review:
        errors = {
            "message": {"Review not found"}
        }
        return errors, 404
    return review.to_dict()


@bp.route("/<int:review_id>", methods=["PUT"])
@login_required
def update_review(review_id):
    review = Review.query.get(review_id)
    if not review:
        return {
            "message": {"Review not found"}
        }, 404

    form = ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if review.buyer_id == current_user.id:
        if form.validate_on_submit():
            review.rating = form.data["rating"]
            review.review = form.data["review"]
            db.session.commit()
            return review.to_dict()
        return {'errors': validation_errors_formatter(form, form.errors)}, 400
    return {
        'errors': {
            'user': "Must own review to update it"
        }
    }, 400


@bp.route("/<int:review_id>", methods=["DELETE"])
@login_required
def delete_review(review_id):
    review = Review.query.get(review_id)
    if not review:
        errors = {
            "message": {"Review not found"}
        }
        return errors, 404

    if review.buyer_id != current_user.id:
        return "You are not authorized to delete this review", 403

    if review.buyer_id == current_user.id:
        db.session.delete(review)
        db.session.commit()
        return {
            "message": "Successfully deleted",
            "statusCode": 200
        }


@bp.route("/current", methods=["GET"])
@login_required
def get_current_reviews():
    """For debugging"""
    reviews = Review.query.filter(Review.buyer_id == current_user.id)
    return [review.to_dict() for review in reviews]


@bp.route("", methods=["GET"])
def get_reviews():
    """For debugging"""
    return [review.to_dict() for review in Review.query]
