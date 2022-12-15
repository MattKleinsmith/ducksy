from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, Product, Review, ProductImage, Order, OrderDetail, Category
from app.forms import ProductForm, ReviewForm, ProductImageForm, validation_errors_formatter
from sqlalchemy.exc import IntegrityError


bp = Blueprint("categories", __name__, url_prefix="/categories")

@bp.route("/<category_id>/products", methods=['GET'])
def get_products_by_category(category_id):
    category = Category.query.get(category_id)

    if category:
        products = []
        for product in category.products:
            categories = [category.name for category in product.categories]
            product = product.to_dict()
            product['categories'] = categories
            products.append(product)
        return products
