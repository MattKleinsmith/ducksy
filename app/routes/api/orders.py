from flask import Blueprint, request
from app.models import db, Order, OrderItem, Product
from flask_login import current_user, login_required

bp = Blueprint("orders", __name__, url_prefix="/orders")


@bp.route("")
@login_required
def get_orders():
    orders = Order.query.filter(Order.user_id == current_user.id)
    return [order.to_dict() for order in orders]


@bp.route("", methods=["POST"])
@login_required
def create_order():
    data = request.get_json()
    product_ids = data['product_ids']
    order = Order(user_id=current_user.id)
    products = Product.query.filter(Product.id.in_(product_ids)).all()
    print(products)

    items = [OrderItem(order=order,
                       product_id=product.id,
                       price=product.price
                       )
             for product in products]
    db.session.add_all(items)
    db.session.commit()
    return {"order_id": order.id}
