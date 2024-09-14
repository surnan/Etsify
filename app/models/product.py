from .db import db, environment,  SCHEMA, add_prefix_for_prod



class Product(db.Model):
    __tablename__ = 'products'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    sellerId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)

    # Relationships
    users = db.relationship('User', back_populates='products')
    reviews = db.relationship('Review', back_populates='products', cascade='all, delete-orphan')
    product_images = db.relationship('ProductImage', back_populates='product', cascade='all, delete-orphan')
    cartproducts = db.relationship('CartProduct', back_populates='products', cascade='all, delete-orphan')
    favorites = db.relationship('Favorite', back_populates='product', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'sellerId': self.sellerId,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'stock': self.stock,
            'product_images': [image.to_dict() for image in self.product_images],
            'reviews': [review.to_dict() for review in self.reviews] 
        }