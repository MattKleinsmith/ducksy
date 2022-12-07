from flask import Blueprint
from . import products, reviews

bp = Blueprint("api", __name__, url_prefix="/api")

bp.register_blueprint(products.bp)
bp.register_blueprint(reviews.bp)
