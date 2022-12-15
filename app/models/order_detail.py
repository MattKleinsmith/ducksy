from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, DateTime, VARCHAR, DECIMAL, TEXT, BOOLEAN
from sqlalchemy.sql import func
from flask_login import UserMixin
#  a crypto library that came with Flask
from werkzeug.security import generate_password_hash, check_password_hash


class OrderDetail(db.Model):
    __tablename__ = "order_details"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey(
        add_prefix_for_prod('orders.id'), name='fk_order_detail_order_id', ondelete='CASCADE'), nullable=False)
    product_id = Column(Integer, ForeignKey(
        add_prefix_for_prod('products.id'), name='fk_order_detail_product_id', ondelete='SET NULL'), nullable=True)
    seller_id = Column(Integer, ForeignKey(
        add_prefix_for_prod('users.id'), name='fk_order_detail_seller_id', ondelete='CASCADE'), nullable=False)
    buyer_id = Column(Integer, ForeignKey(
        add_prefix_for_prod('users.id'), name='fk_order_detail_buyer_id', ondelete='CASCADE'), nullable=False)
    price = Column(DECIMAL, nullable=False)
    quantity = Column(Integer, nullable=False)

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now(),
                        nullable=False)

    order = relationship("Order", back_populates="order_details")
    product = relationship("Product")
    seller = relationship("User", foreign_keys=[seller_id])

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "product": self.product.to_dict() if self.product is not None else None,
            "price": self.price,
            "seller_id": self.seller_id,
            "seller": self.seller.to_dict(),
            "order_id": self.order_id,
            "purchase_date": self.created_at
        }
