from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, Product, Review, ProductImage, Order, OrderDetail, Category
from app.forms import ProductForm, ReviewForm, ProductImageForm, validation_errors_formatter
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
    return {'errors': validation_errors_formatter(form.errors)}, 400


@bp.route("<int:product_id>", methods=['GET'])
def get_product_by_id(product_id):
    try:
        product = Product.query.filter(Product.id == product_id).first()
        return product.to_dict() if product else (f"Product with id {product_id} not found", 404)
    except Exception:
        return "500", 500


@bp.route("<int:product_id>", methods=['PUT'])
@login_required
def put_product(product_id):
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
    return {'errors': validation_errors_formatter(form.errors)}, 400


@bp.route("<int:product_id>", methods=['DELETE'])
@login_required
def delete_product(product_id):
    try:
        # product = Product.query.filter(Product.id == product_id,
        #                                Product.seller_id == current_user.id).first()
        product = db.session.query(Product).filter(
            Product.id == product_id, Product.seller_id == current_user.id).first()
        if (product):
            db.session.delete(product)
            db.session.commit()
            return f"Deleted product with id {product_id}"
        return "404", 404
    except IntegrityError as e:
        print(e)
        return {"error": "Failed to delete"}, 400


@bp.route("<int:product_id>/reviews", methods=['GET'])
def get_reviews_by_product_id(product_id):
    reviews = Review.query.filter(Review.product_id == product_id)
    return [review.to_dict() for review in reviews]


@bp.route("<int:product_id>/reviews", methods=["POST"])
@login_required
def review(product_id):
    # Check database for available product
    product = Product.query.get(product_id)
    if not product:
        return "Product not found", 404
    # Validate seller vs buyer status
    if product.seller_id == current_user.id:
        return "Seller can not leave review for their own products", 400
    reviews = Review.query.filter(
        Review.product_id == product_id, Review.buyer_id == current_user.id).all()
    if len(reviews) > 0:
        return "Buyer already left a review for this product", 400
    # Check if buyer bought the product in order to leave review
    orders = Order.query.filter(Order.buyer_id == current_user.id).all()
    for order in orders:
        if all(map(lambda x: x.product_id != product_id, order.order_details)):
            return "You are not authorized to review this product", 400

    form = ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        review = Review(
            buyer_id=current_user.id,
            seller_id=product.seller_id,
            product_id=product_id,
            rating=int(float(form.data["rating"])),
            review=form.data["review"]
        )
        db.session.add(review)
        db.session.commit()
        return review.to_dict(), 201
    return {'errors': validation_errors_formatter(form.errors)}, 400


@bp.route("<int:product_id>/images", methods=['GET'])
def get_images_by_product_id(product_id):
    product_images = ProductImage.query.filter(
        ProductImage.product_id == product_id)
    return [product_image.to_dict() for product_image in product_images]


@bp.route("<int:product_id>/images", methods=['POST'])
def post_image_by_product_id(product_id):
    form = ProductImageForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = form.data
        product_image = ProductImage(
            product_id=int(product_id),
            url=data['url'],
            preview=data['preview']
        )
        db.session.add(product_image)
        db.session.commit()
        return product_image.to_dict()
    return {'errors': validation_errors_formatter(form.errors)}, 400
