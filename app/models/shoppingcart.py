from .db import db, environment, SCHEMA, add_prefix_for_prod


class Shoppingcart(db.Model):
    __tablename__ = 'shoppingcarts'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)


    userId = db.Column(db.Integer, nullable=False, unique=True)
    # userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Relationships
    # user = db.relationship('User', back_populates='shopping_cart')
    # cart_products = db.relationship('CartProduct', back_populates='shoppingcarts', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.userId
        }