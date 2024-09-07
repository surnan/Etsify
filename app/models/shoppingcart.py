from .db import db, environment, SCHEMA, add_prefix_for_prod
from .cartproduct import CartProduct
# from app.models.cartproduct import CartProduct

class ShoppingCart(db.Model):
    __tablename__ = 'shoppingcarts'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)

    # Relationships
    # user = db.relationship('User', back_populates='shopping_cart')
    user = db.relationship('User', back_populates='shoppingcarts')

    # cart_products = db.relationship('CartProducts', back_populates='shopping_cart', cascade='all, delete-orphan')
    cart_products = db.relationship('CartProduct', back_populates='shopping_cart', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.userId
        }