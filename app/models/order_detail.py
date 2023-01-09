from .db import db

from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, DateTime, DECIMAL
from sqlalchemy.sql import func


class OrderDetail(db.Model):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey(
        'orders.id', name='fk_order_detail_order_id', ondelete='CASCADE'), nullable=False)
    product_id = Column(Integer, ForeignKey(
        'products.id', name='fk_order_detail_product_id', ondelete='SET NULL'), nullable=True)
    seller_id = Column(Integer, ForeignKey(
        'users.id', name='fk_order_detail_seller_id', ondelete='CASCADE'), nullable=False)
    buyer_id = Column(Integer, ForeignKey(
        'users.id', name='fk_order_detail_buyer_id', ondelete='CASCADE'), nullable=False)
    price = Column(DECIMAL, nullable=False)
    quantity = Column(Integer, nullable=False)

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now(),
                        nullable=False)

    order = relationship("Order", back_populates="order_details")
    product = relationship("Product", back_populates="purchases")
    seller = relationship("User", foreign_keys=[seller_id])

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "product": self.product.to_dict() if self.product is not None else None,
            "price": self.price,
            "quantity": self.quantity,
            "seller_id": self.seller_id,
            "seller": self.seller.to_dict(),
            "buyer_id": self.buyer_id,
            "order_id": self.order_id,
            "purchase_date": self.created_at
        }
