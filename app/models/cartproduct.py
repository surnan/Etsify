from .db import db, environment, SCHEMA, add_prefix_for_prod


class CartProduct(db.Model):
    __tablename__ = 'cartproducts'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    shoppingCartId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('shoppingcarts.id')), nullable=False)
    productId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('products.id')), nullable=False)

    # Relationship
    shoppingcarts = db.relationship('ShoppingCart', back_populates='cartproducts')
    products = db.relationship('Product', back_populates='cartproducts')

    def to_dict(self):
        return {
            'id': self.id,
            'shoppingCartId': self.shoppingCartId,
            'productId': self.productId
        }

