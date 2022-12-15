from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, DateTime, VARCHAR, DECIMAL, TEXT, BOOLEAN
from sqlalchemy.sql import func


products_categories = db.Table(
    'products_categories',
    db.Model.metadata,
    db.Column('product_id', db.Integer, db.ForeignKey(
        'products.id', name='fk_product_category_product_id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey(
        'categories.id', name='fk_product_category_category_id'), primary_key=True)
)

if environment == "production":
    products_categories.schema = SCHEMA


class Product(db.Model):
    __tablename__ = "products"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True)

    seller_id = Column(Integer, ForeignKey(
        add_prefix_for_prod('users.id'), name='fk_product_seller_id', ondelete='CASCADE'), nullable=False)

    name = Column(VARCHAR(140), nullable=False)
    price = Column(DECIMAL, nullable=False)
    description = Column(TEXT)

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now(),
                        nullable=False)

    seller = relationship("User", back_populates="products")
    product_images = relationship(
        "ProductImage", cascade="all, delete-orphan", back_populates="product", order_by="ProductImage.id")
    reviews = relationship(
        "Review", back_populates="product", cascade="all, delete-orphan")
    categories = relationship(
        "Category", secondary=products_categories, back_populates="products")

    def to_dict(self):
        preview_images = list(filter(lambda x: x.preview, self.product_images))
        print(self.id, list(map(lambda x: x.id, preview_images)))
        seller_rating = sum(
            [review.rating for review in self.reviews]) / len(self.reviews) if len(self.reviews) > 0 else None
        num_seller_ratings = len(self.reviews)
        return {
            "id": self.id,
            "seller_id": self.seller_id,
            "seller_name": self.seller.display_name,
            "name": self.name,
            "price": str(self.price),
            "description": self.description,
            "preview_image": preview_images[-1].url if len(preview_images) else None,
            "seller": self.seller.to_dict(),
            "seller_rating": seller_rating,
            "num_seller_ratings": num_seller_ratings
        }


class Category(db.Model):
    __tablename__ = "categories"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR, nullable=False)

    products = relationship(
        "Product", secondary=products_categories, back_populates="categories")
