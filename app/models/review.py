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

    author_id = Column(Integer, ForeignKey(
        add_prefix_for_prod('users.id')), nullable=False)
    shop_id = Column(Integer, ForeignKey(add_prefix_for_prod('users.id')))
    product_id = Column(Integer, ForeignKey(
        add_prefix_for_prod('products.id')), nullable=False)
    rating = Column(Integer, nullable=False)
    review = Column(VARCHAR(840), nullable=False)

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now(),
                        nullable=False)

    author = relationship("User", foreign_keys=author_id)
    shop = relationship("User", foreign_keys=shop_id)
    product = relationship("Product", back_populates="reviews")

    def to_dict(self):
        return {
            "id": self.id,
            "author_id": self.author_id,
            "shop_id": self.shop_id,
            "product_id": self.product_id,
            "rating": self.rating,
            "review": self.review
        }
