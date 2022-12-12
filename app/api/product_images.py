from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, Product, Review, ProductImage, Order, OrderDetail
from app.forms import ProductForm, ReviewForm, validation_errors_formatter
from sqlalchemy.exc import IntegrityError

bp = Blueprint("product_images", __name__, url_prefix="product_images")

@bp.route("/<product_image_id>", methods=["DELETE"])
@login_required
def delete_product_image_by_id(product_image_id):
    try:
        product_image = ProductImage.query.get(product_image_id)
        if product_image:
            if product_image.product.seller_id != current_user.id:
                return {'errors': ['Unauthorized']}, 401
            db.session.delete(product_image)
            db.session.commit()
            return f"Deleted product image with id {product_image_id}"
        return "404", 404
    except IntegrityError:
        return "Failed to delete"
