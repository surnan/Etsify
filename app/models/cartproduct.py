from .db import db, environment, SCHEMA, add_prefix_for_prod


class Cartproduct(db.Model):
    __tablename__ = 'cartproducts'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)



    productId = db.Column(db.Integer, nullable=False)
    ##productId needs foreignKey
    

    shoppingCartId = db.Column(db.Integer, db.ForeignKey('shoppingcarts.id'), nullable=False)
    # shoppingCartId = db.Column(db.Integer, nullable=False)


    # Relationship
    shopping_cart = db.relationship('ShoppingCart', back_populates='cartproducts')

    def to_dict(self):
        return {
            'id': self.id,
            'shoppingCartId': self.shoppingCartId,
            'productId': self.productId
        }

