from app.models import db, Favorite, User, Product, environment, SCHEMA
from sqlalchemy.sql import text

def seed_favorites():
    demoFav = Favorite(
        userId='1', productId='1'
    )
    marnieFav = Favorite(
        userId='2', productId='2'
    )
    bobbieFav = Favorite(
        userId='3', productId='3'
    )
    db.session.add(demoFav)
    db.session.add(marnieFav)
    db.session.add(bobbieFav)
    db.session.commit()

def undo_favorites():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.favorites RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM favorites"))
        
    db.session.commit()

    