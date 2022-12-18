from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.schema import Column, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, DateTime, VARCHAR, DECIMAL, TEXT, BOOLEAN
from sqlalchemy.sql import func


products_categories = Table(
    'products_categories',
    db.Model.metadata,
    Column('product_id', Integer, ForeignKey(
        add_prefix_for_prod('products.id'), name='fk_product_category_product_id'), primary_key=True),
    Column('category_id', Integer, ForeignKey(
        add_prefix_for_prod('categories.id'), name='fk_product_category_category_id'), primary_key=True)
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
    purchases = relationship("OrderDetail", back_populates="product")

    def to_dict(self):
        preview_images = list(filter(lambda x: x.preview, self.product_images))
        product_rating = sum(
            [review.rating for review in self.reviews]) / len(self.reviews) if len(self.reviews) > 0 else None
        num_product_ratings = len(self.reviews)
        sales_num = sum([purchase.quantity for purchase in self.purchases])

        return {
            "id": self.id,
            "seller_id": self.seller_id,
            "seller_name": self.seller.display_name,
            "name": self.name,
            "price": str(self.price),
            "description": self.description,
            "preview_image": preview_images[-1].url if len(preview_images) else None,
            "seller": self.seller.to_dict(),
            "product_rating": product_rating,
            "num_product_ratings": num_product_ratings,
            "categories": [x.id for x in self.categories],
            "sales": sales_num,
            "product_images": [x.to_dict() for x in self.product_images]
        }


class Category(db.Model):
    __tablename__ = "categories"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR, nullable=False)

    products = relationship(
        "Product", secondary=products_categories, back_populates="categories")
