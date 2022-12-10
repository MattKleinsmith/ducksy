from flask import Blueprint
from . import products, reviews, session, orders, users

bp = Blueprint("api", __name__, url_prefix="/api")

bp.register_blueprint(session.bp)
bp.register_blueprint(products.bp)
bp.register_blueprint(reviews.bp)
bp.register_blueprint(orders.bp)
bp.register_blueprint(users.bp)
