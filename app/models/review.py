from .db import db, environment, SCHEMA, add_prefix_for_prod

from .db import db, environment, SCHEMA, add_prefix_for_prod

class Review(db.Model):
    __tablename__ = add_prefix_for_prod('reviews')

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(255), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    productId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('products.id')), nullable=False)

    # Relationships
    user = db.relationship('User', back_populates='review')
    product = db.relationship('Product', back_populates='reviews')

    def to_dict(self):
        return {
            'id': self.id,
            'stars': self.stars,
            'review': self.review,
            'userId': self.userId,
            'productId': self.productId
        }



# class Review(db.Model):
#     __tablename__ = 'reviews'

#     if environment == "production":
#         __table_args__ = {'schema': SCHEMA}

#     id = db.Column(db.Integer, primary_key=True)
#     stars = db.Column(db.Integer, nullable=False)
#     review = db.Column(db.String(255), nullable=False)

#     userId = db.Column(db.Integer, nullable=False)
#     # userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    

#     productId = db.Column(db.Integer, nullable=False)
#     # productId = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)




#     # Relationships
#     # user = db.relationship('User', back_populates='review')
#     # product = db.relationship('Product', back_populates='reviews')

#     def to_dict(self):
#         return {
#             'id': self.id,
#             'stars': self.stars,
#             'review': self.review,
#             'userId': self.userId,
#             'productId': self.productId
#         }
