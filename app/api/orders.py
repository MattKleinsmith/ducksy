from flask import Blueprint, request
from app.models import db, Order, OrderProduct, Product
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
    products = Product.query.filter(Product.id.in_(product_ids)).all()
    order = Order(buyer_id=current_user.id, seller_id=products[0].seller_id)
    print(order, '==============================')
    order_products = [OrderProduct(order=order,
                       product_id=product.id,
                       price=product.price
                       )
             for product in products]
    db.session.add_all(order_products)
    db.session.commit()
    return {"order_id": order.id}

# this just for removing order to test some functionality
# @bp.route("/<order_id>", methods=['delete'])
# @login_required
# def delete_order(order_id):
#     order = Order.query.get(order_id)
#     items = OrderProduct.query.all()
#     for item in items:
#         db.session.delete(item)
#     db.session.delete(order)
#     db.session.commit()
#     return "hi"
