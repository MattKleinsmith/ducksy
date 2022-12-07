from flask import Blueprint
from app.models import Product, Review

bp = Blueprint("products", __name__, url_prefix="/products")


@bp.route("/")
def products():
    products = Product.query
    return [product.to_dict() for product in products]


@bp.route("<product_id>")
def product_by_id(product_id):
    return Product.query.filter(Product.id == product_id).first().to_dict()


@bp.route("<product_id>/reviews")
def reviews_by_product_id(product_id):
    reviews = Review.query.filter(Review.product_id == product_id)
    return [review.to_dict() for review in reviews]
