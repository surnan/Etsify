from .db import db, environment, SCHEMA

class ShoppingCart(db.Model):
    __tablename__ = 'shopping_carts'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relationship with CartProduct
    cart_products = db.relationship('CartProduct', backref='shopping_cart', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'products': [cart_product.to_dict() for cart_product in self.cart_products]
        }

class CartProduct(db.Model):
    __tablename__ = 'cart_products'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    shopping_cart_id = db.Column(db.Integer, db.ForeignKey('shopping_carts.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    # Relationship with Product
    product = db.relationship('Product', backref='cart_products')

    def to_dict(self):
        return {
            'id': self.id,
            'shopping_cart_id': self.shopping_cart_id,
            'product': self.product.to_dict(),  # Assuming Product has a `to_dict` method
            'quantity': self.quantity
        }
