from flask import Blueprint
from flask_login import login_required, current_user
from app.models import db, Review
from app.forms import ReviewForm
from sqlalchemy.exc import IntegrityError


bp = Blueprint("reviews", __name__, url_prefix="/reviews")


@bp.route("/<int:review_id>", methods=["patch"])
def update_review(review_id):
    form = ReviewForm()
    review_tobe_updated = Review.query.get(review_id)

    if form.validate_on_submit():
        review_tobe_updated.rating = form.data["rating"]
        review_tobe_updated.review = form.data["review"]
        db.session.commit()

    if form.errors:
        return {"errors": form.errors}, 400, {"Content-Type": "application/json"}

    return {"review": review_tobe_updated.to_dict()}, 200, {"Content-Type": "application/json"}


@bp.route("/<int:review_id>", methods=["delete"])
def delete_review(review_id):
    review_tobe_deleted = Review.query.get(review_id)
    db.session.delete(review_tobe_deleted)
    db.session.commit()
    return {
        "message": "Successfully deleted",
        "statusCode": 200
    }, 200, {"Content-Type": "application/json"}
