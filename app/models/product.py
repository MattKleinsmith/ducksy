from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, DateTime, VARCHAR, DECIMAL, TEXT, BOOLEAN
from sqlalchemy.sql import func


products_categories = db.Table(
    'products_categories',
    db.Model.metadata,
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True)
)

if environment == "production":
    products_categories.schema = SCHEMA



class Product(db.Model):
    __tablename__ = "products"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True)

    seller_id = Column(Integer, ForeignKey(
        add_prefix_for_prod('users.id'), name='fk_product_seller_id'), nullable=False)

    name = Column(VARCHAR(140), nullable=False)
    price = Column(DECIMAL, nullable=False)
    description = Column(TEXT)

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now(),
                        nullable=False)

    seller = relationship("User", back_populates="products")
    product_images = relationship("ProductImage", back_populates="product")
    reviews = relationship("Review", back_populates="product")
    categories = relationship("Category", secondary=products_categories, back_populates="products")
    orders_details = relationship("OrderDetail", back_populates='product')



    def to_dict(self):
        return {
            "id": self.id,
            "seller_id": self.seller_id,
            "seller_name": self.seller.display_name,
            "name": self.name,
            "price": str(self.price),
            "description": self.description,
            "preview_image": self.product_images[0].url if len(self.product_images) else None
        }


class Category(db.Model):
    __tablename__ = "categories"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR, nullable=False)

    products = relationship("Product", secondary=products_categories, back_populates="categories")
