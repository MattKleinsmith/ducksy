from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, Product, Review, ProductImage, Order, OrderDetail
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
            [review.rating for review in reviews]) / len(reviews) if len(reviews) > 0 else None
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


@bp.route("<int:product_id>", methods=['GET'])
def get_product_by_id(product_id):
    try:
        product = Product.query.filter(Product.id == product_id).first()
        return product.to_dict() if product else (f"Product with id {product_id} not found", 404)
    except Exception:
        return "500", 500


@bp.route("/<product_id>", methods=['PUT'])
@login_required
def patch_product(product_id):
    try:
        product = Product.query.filter(Product.id == product_id,
                                       Product.seller_id == current_user.id).first()
        if (not product):
            return "404", 404
        form = ProductForm()
        form['csrf_token'].data = request.cookies['csrf_token']
        if form.validate_on_submit():
            product.name = form.name.data
            product.price = form.price.data
            product.description = form.description.data
            db.session.commit()
            return product.to_dict()
        return {"errors": form.errors}, 400
    except IntegrityError:
        return "Failed to put", 500


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
    product = Product.query.get(product_id)
    if product is None:
        return "No product", 404
    if product.seller_id == current_user.id:
        return "Seller can not leave review for your products", 404

    form = ReviewForm()
    # form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        new_review = Review(
                            buyer_id=current_user.id,
                            seller_id=product.seller_id,
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


@bp.route("fun", methods=['GET'])
def show_product_images():
    html = ''
    images = ProductImage.query
    for image in images:
        html += f"<img src='{image.url}' />"
    return html
