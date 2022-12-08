from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, DateTime, VARCHAR, DECIMAL, TEXT, BOOLEAN
from sqlalchemy.sql import func
from flask_login import UserMixin
#  a crypto library that came with Flask
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


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

    products = relationship("Product", back_populates="user")
    reviews = relationship("Review", back_populates="user")
    orders = relationship("Order", back_populates="user")

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


class Product(db.Model):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(VARCHAR(140), nullable=False)
    price = Column(DECIMAL, nullable=False)
    description = Column(TEXT)

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now(),
                        nullable=False)

    user = relationship("User", back_populates="products")
    product_images = relationship("ProductImage", back_populates="product")
    reviews = relationship("Review", back_populates="product")
    items = relationship("OrderItem", back_populates="product")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "price": self.price,
            "description": self.description
        }


class ProductImage(db.Model):
    __tablename__ = "product_images"

    id = Column(Integer, primary_key=True)

    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    url = Column(TEXT, nullable=False)
    preview = Column(BOOLEAN, nullable=False)

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now(),
                        nullable=False)

    product = relationship("Product", back_populates="product_images")

    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "url": self.url,
            "preview": self.preview
        }


class Review(db.Model):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    review = Column(VARCHAR(840), nullable=False)

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now(),
                        nullable=False)

    user = relationship("User", back_populates="reviews")
    product = relationship("Product", back_populates="reviews")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "product_id": self.product_id,
            "rating": self.rating,
            "review": self.review
        }


class Order(db.Model):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now(),
                        nullable=False)

    items = relationship("OrderItem", back_populates="order")
    user = relationship("User", back_populates="orders")

    def to_dict(self):
        return {
            "id": self.id,
            "order_details": [item.to_dict() for item in self.items]
        }


class OrderItem(db.Model):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    price = Column(DECIMAL, nullable=False)
    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now(),
                        nullable=False)

    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="items")

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "price": self.price
        }
