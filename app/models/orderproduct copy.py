from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class OrderProduct(db.Model):
    __tablename__ = 'orderproducts'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    orderId = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    productId = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    order = db.relationship('Orders', back_populates='order_products')
    product = db.relationship('Products', back_populates='order_products')

    def to_dict(self):
        return {
            'id': self.id,
            'orderId': self.orderId,
            'productId': self.productId,
            'created_at': self.created_at
        }