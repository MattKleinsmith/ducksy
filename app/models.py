from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import Column
from sqlalchemy.orm import ForeignKey, relationship
from sqlalchemy.types import Integer, String, DateTime, Float
from flask_login import UserMixin
#  a crypto library that came with Flask
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class Product(db.Model):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String(140), nullable=False)
    price = Column(Float(asdecimal=True), nullable=False)
    description = Column(String(5000), nullable=False)

    user = relationship("Product", back_populates="products")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "price": self.price,
            "description": self.description
        }


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    display_name = Column(String(255), nullable=False)
    email = Column(String(100), unique=True)
    profile_picture = Column(String(255))
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    products = relationship("Product", back_populates="user")

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
            "profile_picture": self.profile_picture,
        }
