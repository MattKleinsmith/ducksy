from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, DateTime, VARCHAR, TEXT
from sqlalchemy.sql import func
from flask_login import UserMixin
#  a crypto library that came with Flask
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    display_name = Column(VARCHAR(100), nullable=False)
    email = Column(VARCHAR(100), nullable=False, unique=True)
    hashed_password = Column(TEXT, nullable=False)
    profile_picture_url = Column(
        TEXT, server_default="https://d23.com/app/uploads/2017/10/1180w-600h_101717_donald-nephews-anniversary_v3-780x440.jpg")

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now(),
                        nullable=False)

    products = relationship("Product", back_populates="seller")
    # buyer_orders = relationship(
    #     "Order", back_populates="buyer", foreign_keys=[Order.buyer_id])

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            "id": self.id,
            "display_name": self.display_name,
            "email": self.email,
            "profile_picture_url": self.profile_picture_url,
        }
