from flask import Blueprint, request
from app.models import db, Order, OrderDetail, Product
from flask_login import current_user, login_required

bp = Blueprint("orders", __name__, url_prefix="/orders")


@bp.route("", methods=["POST"])
@login_required
def create_order():
    data = request.get_json()
    product_ids = data['product_ids']
    if len(product_ids) == 0:
        return "No products given", 400
    products = Product.query.filter(Product.id.in_(product_ids)).all()
    if len(products) == 0:
        return "No products found", 404
    # user cannot buy their own products
    seller_ids = (product.seller_id for product in products)
    if current_user.id in seller_ids:
        return "Seller can't order their own product", 401
    order = Order(buyer_id=current_user.id)
    order_products = [OrderDetail(order=order,
                                  product_id=product.id,
                                  seller_id=product.seller_id,
                                  price=product.price)
                      for product in products]
    db.session.add_all(order_products)
    db.session.commit()
    return {"order_id": order.id}


@bp.route("/<order_id>", methods=['DELETE'])
@login_required
def delete_order(order_id):
    order = Order.query.get(order_id)
    order_items = OrderDetail.query.filter(
        OrderDetail.order_id == order.id).all()
    for order_item in order_items:
        db.session.delete(order_item)
    db.session.delete(order)
    db.session.commit()
    return "Success"
