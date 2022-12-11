from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, Product, Review, ProductImage, Order, OrderProduct
from app.forms import ProductForm, ReviewForm, validation_errors_formatter
from sqlalchemy.exc import IntegrityError

bp = Blueprint("products", __name__, url_prefix="/products")


@bp.route("/", methods=['GET'])
def get_products():
    products = []
    for product in Product.query:
        reviews = product.reviews
        product = product.to_dict()
        product["seller_rating"] = sum(
            [review.rating for review in reviews]) / len(reviews)
        product["num_seller_ratings"] = len(reviews)
        products.append(product)
    return products


@bp.route("/", methods=['POST'])
@login_required
def post_product():
    form = ProductForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if (form.validate_on_submit()):
        product = Product(
            seller=current_user,
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
                                       Product.seller_id == current_user.id).first()
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
                                       Product.seller_id == current_user.id)
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


@bp.route("/<int:product_id>/reviews", methods=["post"])
@login_required
def review(product_id):
    orders = current_user.orders
    if len(orders) > 0:
        for order in orders:
            for order in order.items:
                if order.product_id == product_id:
                    form = ReviewForm()
                    if form.validate_on_submit():
                        new_review = Review(
                            buyer_id=current_user.id,
                            seller_id=order.product_id,
                            product_id=product_id,
                            rating=form.data["rating"],
                            review=form.data["review"]
                        )
                        db.session.add(new_review)
                        db.session.commit()
                        return new_review.to_dict(), 201
                    if form.errors:
                        return {
                            "message": "Validation Error",
                            "statusCode": 400,
                            "errors": form.errors
                        }, 400, {"Content-Type": "application/json"}
                    return "Fail to create review", 404
        return "Fail to create review", 404


@bp.route("fun", methods=['GET'])
def show_product_images():
    html = ''
    images = ProductImage.query
    for image in images:
        html += f"<img src='{image.url}' />"
    return html
