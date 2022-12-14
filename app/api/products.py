from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, Product, Review, ProductImage, Order, OrderDetail, Category
from app.forms import ProductForm, ReviewForm, ProductImageForm, validation_errors_formatter
from sqlalchemy.exc import IntegrityError
from app.seeds.upload import upload_image_to_bucket_from_url, upload_image_to_bucket
from werkzeug.utils import secure_filename

bp = Blueprint("products", __name__, url_prefix="/products")


@bp.route("", methods=['GET'])
def get_products():
    query = request.args.getlist("categories")
    if query:
        products = []
        query_params = query[0].split(', ')
        categories = Category.query.filter(
            Category.name.in_(query_params)).all()
        query_categories = [category.name for category in categories]

        for category in categories:
            for product in category.products:
                product_categories = [
                    category.name for category in product.categories]
                if product_categories == query_categories:
                    product = product.to_dict()
                    product['categories'] = product_categories
                    products.append(product)
        return products
    else:
        return [product.to_dict() for product in Product.query]


@bp.route("", methods=['POST'])
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
            print("-"*50)
            print("Deleting PRODUCT:", product.to_dict())
            print("-"*75)
            db.session.delete(product)
            db.session.commit()
            return {"message": f"Deleted product with id {product_id}"}
        return "404", 404
    except IntegrityError as e:
        print(e)
        return {"errors": {
            "server": "Server failed to delete"
        }}, 500


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
        return {'errors': "Product not found"}, 404
    # Validate seller vs buyer status
    if product.seller_id == current_user.id:
        return {"errors": "Seller can not leave review for their own products"}, 400
    reviews = Review.query.filter(
        Review.product_id == product_id, Review.buyer_id == current_user.id).all()
    if len(reviews) > 0:
        error_message = {
            'errors': {
                'message': "Buyer already left a review for this product"
            }
        }
        return error_message, 400
    # Check if buyer bought the product in order to leave review
    orders = Order.query.filter(Order.buyer_id == current_user.id).all()
    for order in orders:
        for product_info in order.order_details:
            if product_id == product_info.product_id:
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
    error_message = {
        'errors': {
            'message': "A user can only review a product they've purchased"}}
    return error_message, 400


@bp.route("<int:product_id>/images", methods=['GET'])
def get_images_by_product_id(product_id):
    product_images = ProductImage.query.filter(
        ProductImage.product_id == product_id)
    return [product_image.to_dict() for product_image in product_images]


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename): return '.' in filename and filename.rsplit(
    '.', 1)[1].lower() in ALLOWED_EXTENSIONS


@bp.route("<int:product_id>/images", methods=['POST'])
def post_image_by_product_id(product_id):
    try:
        file = request.files['image']
        filename = secure_filename(file.filename)
        if not allowed_file(filename):
            return {
                "errors": {
                    "image": "Please upload a supported image format: .png and .jpg"
                }
            }, 400
        url = upload_image_to_bucket(file, filename)
        product_image = ProductImage(
            product_id=product_id,
            url=url,
            preview=request.form['preview'] == 'true'
        )
        db.session.add(product_image)
        db.session.commit()
        return product_image.to_dict()
    except Exception as e:
        return {
            "errors": {
                "image": str(e)
            }
        }, 500
