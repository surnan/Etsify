from app.models import db, review, environment, SCHEMA
from reviews import Review
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_reviews():
    rev1 = Review(
        stars=5, review='Great concise instructions for how to use', user_id = 1, product_id = 1)
    rev2= Review(
        stars=5, review='Amazing', user_id = 1, product_id = 1)
    rev3 = Review(
        stars=5, review='Cozy and Nice', user_id = 1, product_id = 1)
    rev4 = Review(
        stars=5, review='Great product', user_id = 1, product_id = 1)
    rev5= Review(
        stars=5, review='Amazing', user_id = 1, product_id = 1)
    rev6 = Review(
        stars=5, review='Beautiful and ornate', user_id = 2, product_id = 2)
    rev7 = Review(
        stars=5, review='Aesthetically and amazing', user_id = 2, product_id = 2)
    rev8 = Review(
        stars=5, review='Intricate and nicely decorated', user_id = 2, product_id = 2)
    rev9 = Review(
        stars=5, review='Efficient and easy to figure how to use', user_id = 2, product_id = 2)
    rev10 = Review(
        stars=5, review='Beautifully decorated and easy to use', user_id = 2, product_id = 2)
    

    db.session.add(rev1)
    db.session.add(rev2)
    db.session.add(rev3)
    db.session.add(rev4)
    db.session.add(rev5)
    db.session.add(rev6)
    db.session.add(rev7)
    db.session.add(rev8)
    db.session.add(rev9)
    db.session.add(rev10)
    db.session.commit()