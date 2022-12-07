from flask import Blueprint
from flask_login import login_required, current_user
from app.models import db, Product, Review
from app.forms import ProductForm

bp = Blueprint("products", __name__, url_prefix="/products")


@bp.route("/")
def get_products():
    products = Product.query
    return [product.to_dict() for product in products]


@bp.route("/", methods=['POST'])
@login_required
def post_product():
    form = ProductForm()
    if (form.validate_on_submit()):
        product = Product(
            user=current_user,
            name=form.name.data,
            price=form.price.data,
            description=form.description.data
        )
        db.session.add(product)
        db.session.commit()
        return product.to_dict(), 201
    return "failed to post"


@bp.route("<product_id>")
def product_by_id(product_id):
    return Product.query.filter(Product.id == product_id).first().to_dict()


@bp.route("<product_id>/reviews")
def reviews_by_product_id(product_id):
    reviews = Review.query.filter(Review.product_id == product_id)
    return [review.to_dict() for review in reviews]
