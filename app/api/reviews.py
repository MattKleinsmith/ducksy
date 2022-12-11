from flask import Blueprint
from flask_login import login_required, current_user
from app.models import db, Review
from app.forms import ReviewForm
from sqlalchemy.exc import IntegrityError


bp = Blueprint("reviews", __name__, url_prefix="/reviews")


@bp.route("/<int:review_id>", methods=["patch"])
@login_required
def update_review(review_id):
    form = ReviewForm()
    review_tobe_updated = Review.query.get(review_id)

    if review_tobe_updated and review_tobe_updated.buyer_id == current_user.id:
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


@bp.route("/<int:review_id>", methods=["delete"])
@login_required
def delete_review(review_id):
    review_tobe_deleted = Review.query.get(review_id)
    if review_tobe_deleted and review_tobe_deleted.buyer_id == current_user.id:
        db.session.delete(review_tobe_deleted)
        db.session.commit()
        return {
            "message": "Successfully deleted",
            "statusCode": 200
        }, 200, {"Content-Type": "application/json"}
    return "Fail to delete", 404
