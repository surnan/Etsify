from app.models import db, Review, environment, SCHEMA

from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_reviews():
    rev1 = Review(
        stars=5, review='Great concise instructions for how to use', userId = 1, productId = 1)
    rev2= Review(
        stars=5, review='Amazing', userId = 1, productId = 1)
    rev3 = Review(
        stars=5, review='Cozy and Nice', userId = 1, productId = 1)
    rev4 = Review(
        stars=5, review='Great product', userId= 1, productId = 1)
    rev5= Review(
        stars=5, review='Amazing', userId = 1, productId = 1)
    rev6 = Review(
        stars=5, review='Beautiful and ornate', userId = 2, productId = 2)
    rev7 = Review(
        stars=5, review='Aesthetically and amazing', userId = 2, productId = 2)
    rev8 = Review(
        stars=5, review='Intricate and nicely decorated', userId = 2, productId = 2)
    rev9 = Review(
        stars=5, review='Efficient and easy to figure how to use', userId = 2, productId = 2)
    rev10 = Review(
        stars=5, review='Beautifully decorated and easy to use', userId = 2, productId = 2)
    

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

def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))
        
    db.session.commit()