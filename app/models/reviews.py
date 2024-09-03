from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash


class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Integer)
    review = db.Column(db.String(255))
    product_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)