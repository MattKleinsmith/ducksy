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


class Review(db.Model):
    __tablename__ = "reviews"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True)

    buyer_id = Column(Integer, ForeignKey(
        add_prefix_for_prod('users.id'), name='fk_review_buyer_id', ondelete='CASCADE'), nullable=False)
    seller_id = Column(Integer, ForeignKey(
        add_prefix_for_prod('users.id'), name='fk_review_seller_id', ondelete='CASCADE'))
    product_id = Column(Integer, ForeignKey(
        add_prefix_for_prod('products.id'), name='fk_review_product_id', ondelete='CASCADE'), nullable=False)
    rating = Column(Integer, nullable=False)
    review = Column(VARCHAR(840), nullable=False)

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now(),
                        nullable=False)

    buyer = relationship("User", foreign_keys=[buyer_id])
    product = relationship("Product", back_populates="reviews")

    def to_dict(self):
        return {
            "id": self.id,
            "buyer_id": self.buyer_id,
            "buyer": self.buyer.to_dict(),
            "seller_id": self.seller_id,
            "product_id": self.product_id,
            "rating": self.rating,
            "review": self.review,
            "created_at": self.created_at
        }
