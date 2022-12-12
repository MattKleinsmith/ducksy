from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, Review
from app.forms import ReviewForm
from sqlalchemy.exc import IntegrityError


bp = Blueprint("reviews", __name__, url_prefix="/reviews")


@bp.route("/<int:review_id>", methods=["GET"])
def get_review(review_id):
    review = Review.query.get(review_id)
    if not review:
        return "Review not found", 404
    return review.to_dict()


@bp.route("/<int:review_id>", methods=["PUT"])
@login_required
def update_review(review_id):
    review_tobe_updated = Review.query.get(review_id)
    print(review_tobe_updated)
    if review_tobe_updated is None:
        return "No review", 404

    form = ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if review_tobe_updated.buyer_id == current_user.id:
        if form.validate_on_submit():
            review_tobe_updated.rating = form.data["rating"]
            review_tobe_updated.review = form.data["review"]
            db.session.commit()
            return {
                "rating": review_tobe_updated.rating,
                "review": review_tobe_updated.review
            }, 201

        if form.errors:
            return {
                "message": "Validation Error",
                "statusCode": 400,
                "errors": form.errors
            }, 400, {"Content-Type": "application/json"}
    return "Fail to update", 404


@bp.route("/<int:review_id>", methods=["DELETE"])
@login_required
def delete_review(review_id):
    review = Review.query.get(review_id)
    if not review:
        return "Review not found", 404
    if review.buyer_id != current_user.id:
        return "You are not authorized to delete this review", 403

    if review.buyer_id == current_user.id:
        db.session.delete(review)
        db.session.commit()
        return {
            "message": "Successfully deleted",
            "statusCode": 200
        }, 200, {"Content-Type": "application/json"}


@bp.route("/current", methods=["GET"])
def get_current_reviews():
    """For debugging"""
    reviews = Review.query.filter(Review.buyer_id == current_user.id)
    return [review.to_dict() for review in reviews]


@bp.route("", methods=["GET"])
def get_reviews():
    """For debugging"""
    return [review.to_dict() for review in Review.query]
