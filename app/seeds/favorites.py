from app.models import db, Favorite, User, Product, environment, SCHEMA
from sqlalchemy.sql import text

def seed_favorites():
    demoFav = User(
        user_id='1', product_id='1'
    )
    marnieFav = User(
        user_id='2', product_id='2'
    )
    bobbieFav = User(
        user_id='3', product_id='3'
    )
    db.session.add(demoFav)
    db.session.add(marnieFav)
    db.session.add(bobbieFav)
    db.session.commit()

def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.favorites RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM favorites"))
        
    db.session.commit()

    