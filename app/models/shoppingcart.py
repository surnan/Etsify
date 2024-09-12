from .db import db, environment, SCHEMA, add_prefix_for_prod
from .cartproduct import CartProduct
# from app.models.cartproduct import CartProduct

class ShoppingCart(db.Model):
    __tablename__ = 'shoppingcarts'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    
    # Relationships
    users = db.relationship('User', back_populates='shoppingcarts')
    cartproducts = db.relationship('CartProduct', back_populates='shoppingcarts', cascade='all, delete-orphan')


    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.userId
        }