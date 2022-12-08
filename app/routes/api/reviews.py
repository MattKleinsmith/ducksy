from flask import Blueprint
from app.models import Review

bp = Blueprint("reviews", __name__, url_prefix="/reviews")


@bp.route("")
def reviews():
    reviews = Review.query
    return [review.to_dict() for review in reviews]
