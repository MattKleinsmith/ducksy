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


class Order(db.Model):
    __tablename__ = "orders"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey(
        add_prefix_for_prod('users.id'), name='fk_order_customer_id'), nullable=False)
    shop_id = Column(Integer, ForeignKey(
        add_prefix_for_prod('users.id'), name='fk_order_shop_id'), nullable=False)
    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now(),
                        nullable=False)

    items = relationship("OrderItem", back_populates="order")
    shop = relationship("User", back_populates="shop_orders", foreign_keys=[shop_id])
    customer = relationship("User", back_populates="customer_orders", foreign_keys=[customer_id])

    def to_dict(self):
        return {
            "id": self.id,
            "order_details": [item.to_dict() for item in self.items]
        }
