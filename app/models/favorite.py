from .db import db, environment, SCHEMA

class Favorite(db.Model):
    __tablename__ = 'favorites'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    #Create Columns
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    productId = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)

    #Relationship
    user = db.relationship("User", back_populates="favorites")
    product = db.relationship("Product", back_populates="favorites")

    #Format
    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'productId': self.productId
        }