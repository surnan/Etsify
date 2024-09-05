from .db import db, environment, SCHEMA, add_prefix_for_prod

class Order(db.Model):
    __tablename__ = 'orders'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relationships
    user = db.relationship('User', back_populates='orders')
    order_products = db.relationship('OrderProduct', back_populates='order', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.userId
        }