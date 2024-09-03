from .db import db, environment, SCHEMA

class Order(db.Model):
    __tablename__ = 'orders'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())

    # Relationship with OrderProduct
    order_products = db.relationship('OrderProduct', backref='order', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat(),
            'products': [order_product.to_dict() for order_product in self.order_products]
        }

class OrderProduct(db.Model):
    __tablename__ = 'order_products'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    # Relationship with Product
    product = db.relationship('Product', backref='order_products')

    def to_dict(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'product': self.product.to_dict(),  # Assuming Product has a `to_dict` method
            'quantity': self.quantity
        }
