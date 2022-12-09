from flask import Blueprint
from flask_login import login_required, current_user
from app.models import db, Product, Review, ProductImage
from app.forms import ProductForm
from sqlalchemy.exc import IntegrityError

bp = Blueprint("products", __name__, url_prefix="/products")


@bp.route("/")
def get_products():
    return [product.to_dict() for product in Product.query]


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
    return "Failed to post"


@bp.route("<product_id>")
def product_by_id(product_id):
    return Product.query.filter(Product.id == product_id).first().to_dict()


@bp.route("/<product_id>", methods=['PATCH'])
@login_required
def patch_product(product_id):
    try:
        form = ProductForm()
        product = Product.query.filter(Product.id == product_id,
                                       Product.user_id == current_user.id).first()
        if (product):
            product.name = form.name.data if form.name.data else product.name
            product.price = form.price.data if form.price.data else product.price
            product.description = form.description.data if form.description.data else product.description
            db.session.commit()
            return product.to_dict()
        return "404", 404
    except IntegrityError:
        return "Failed to patch"


@bp.route("/<product_id>", methods=['DELETE'])
@login_required
def delete_product(product_id):
    try:
        product = Product.query.filter(Product.id == product_id,
                                       Product.user_id == current_user.id)
        if (product.first()):
            product.delete()
            db.session.commit()
            return f"Deleted product with id {product_id}"
        return "404", 404
    except IntegrityError:
        return "Failed to delete"


@bp.route("<product_id>/reviews")
def reviews_by_product_id(product_id):
    reviews = Review.query.filter(Review.product_id == product_id)
    return [review.to_dict() for review in reviews]


@bp.route("fun")
def show_product_images():
    html = ''
    images = ProductImage.query
    for image in images:
        html += f"<img src='{image.url}' />"
    return html
