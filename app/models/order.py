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
    buyer_id = Column(Integer, ForeignKey(
        add_prefix_for_prod('users.id'), name='fk_order_buyer_id'), nullable=False)
    seller_id = Column(Integer, ForeignKey(
        add_prefix_for_prod('users.id'), name='fk_order_seller_id'), nullable=False)
    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now(),
                        nullable=False)

    # orders_products = relationship("OrderProduct", back_populates="order")

    def to_dict(self):
        return {
            "id": self.id,
            "order_details": [item.to_dict() for item in self.items]
        }
