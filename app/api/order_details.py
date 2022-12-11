from flask import Blueprint, request
from app.models import db, Order, OrderDetail, Product
from flask_login import current_user, login_required

bp = Blueprint("order_details", __name__, url_prefix="/order_details")


@bp.route("/current")
@login_required
def get_order_details():
    orders = Order.query.filter(Order.buyer_id == current_user.id)
    order_ids = [order.id for order in orders]
    order_details = OrderDetail.query.filter(
        OrderDetail.order_id.in_(order_ids))
    return [order_detail.to_dict() for order_detail in order_details]
