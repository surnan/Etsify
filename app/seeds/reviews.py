from app.models import db, reviews, environment, SCHEMA
from reviews import Review
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_reviews():
    rev1 = Review(
        stars=5, review='Great place', user_id = 1, product_id = 1)
    rev2= Review(
        stars=5, review='Amazing', user_id = 1, product_id = 1)
    rev3 = Review(
        stars=5, review='Cozy and Nice', user_id = 1, produce_id = 1)

    db.session.add(rev1)
    db.session.add(rev2)
    db.session.add(rev3)
    db.session.commit()