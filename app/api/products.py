from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, Product, Review, ProductImage
from app.forms import ProductForm, validation_errors_formatter
from sqlalchemy.exc import IntegrityError

bp = Blueprint("products", __name__, url_prefix="/products")


@bp.route("/", methods=['GET'])
def get_products():
    products = []
    for product in Product.query:
        product = product.to_dict()
        reviews = Review.query.filter(
            Review.shop_id == product["shop_id"]).all()
        product["shop_rating"] = sum(
            [review.rating for review in reviews]) / len(reviews)
        product["num_shop_ratings"] = len(reviews)
        products.append(product)
    return products


@bp.route("/", methods=['POST'])
@login_required
def post_product():
    form = ProductForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if (form.validate_on_submit()):
        product = Product(
            shop=current_user,
            name=form.name.data,
            price=form.price.data,
            description=form.description.data
        )
        db.session.add(product)
        db.session.commit()
        return product.to_dict(), 201
    return "Failed to post"


@bp.route("<product_id>", methods=['GET'])
def get_product_by_id(product_id):
    product = Product.query.filter(Product.id == product_id).first()
    return product.to_dict() if product else ("Not found", 404)


@bp.route("/<product_id>", methods=['PUT'])
@login_required
def patch_product(product_id):
    try:
        form = ProductForm()
        product = Product.query.filter(Product.id == product_id,
                                       Product.shop_id == current_user.id).first()
        if form.validate_on_submit():
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
                                       Product.shop_id == current_user.id)
        if (product.first()):
            product.delete()
            db.session.commit()
            return f"Deleted product with id {product_id}"
        return "404", 404
    except IntegrityError:
        return "Failed to delete"


@bp.route("<product_id>/reviews", methods=['GET'])
def get_reviews_by_product_id(product_id):
    reviews = Review.query.filter(Review.product_id == product_id)
    return [review.to_dict() for review in reviews]


@bp.route("fun", methods=['GET'])
def show_product_images():
    html = ''
    images = ProductImage.query
    for image in images:
        html += f"<img src='{image.url}' />"
    return html
