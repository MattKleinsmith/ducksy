from .db import db

from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, DateTime
from sqlalchemy.sql import func


class Order(db.Model):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    buyer_id = Column(Integer, ForeignKey(
        'users.id', name='fk_order_buyer_id', ondelete='CASCADE'), nullable=False)
    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now(),
                        nullable=False)

    order_details = relationship("OrderDetail", back_populates="order")

    def to_dict(self):
        return {
            "id": self.id,
            "order_details": [order_detail.to_dict() for order_detail in self.order_details],
        }
