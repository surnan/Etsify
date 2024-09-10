
from .db import db, environment, SCHEMA, add_prefix_for_prod


class Favorite(db.Model):
    __tablename__ = 'favorites'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer, nullable=False)


    # userId = db.Column(db.Integer, nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    # Relationship
    user = db.relationship('User', back_populates='favorites')

    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'productId': self.productId
        }
