from .db import db, environment, SCHEMA, add_prefix_for_prod


class CartProduct(db.Model):
    __tablename__ = 'cartproducts'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    shoppingCartId = db.Column(db.Integer, db.ForeignKey('shoppingcarts.id'), nullable=False)
    productId = db.Column(db.Integer, nullable=False)

    # Relationship
    shopping_cart = db.relationship('ShoppingCart', back_populates='cart_products')

    def to_dict(self):
        return {
            'id': self.id,
            'shoppingCartId': self.shoppingCartId,
            'productId': self.productId,
            'created_at': self.created_at
        }

