from .db import db, environment, SCHEMA, add_prefix_for_prod

class Review(db.Model):
    __tablename__ = 'reviews'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(255), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    productId = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)

    # Relationships
    user = db.relationship('User', back_populates='reviews')
    product = db.relationship('Products', back_populates='reviews')

    def to_dict(self):
        return {
            'id': self.id,
            'stars': self.stars,
            'review': self.review,
            'userId': self.userId,
            'productId': self.productId
        }
