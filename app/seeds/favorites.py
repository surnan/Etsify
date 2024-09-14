from app.models import db, Favorite, environment, SCHEMA
from sqlalchemy.sql import text

def seed_favorites():
    # demoFav = Favorite(
    #     userId='1', productId='1'
    # )
    # marnieFav = Favorite(
    #     userId='2', productId='2'
    # )
    # bobbieFav = Favorite(
    #     userId='3', productId='3'
    # )
    # db.session.add(demoFav)
    # db.session.add(marnieFav)
    # db.session.add(bobbieFav)

    # User 1 favorites Product 1 and Product 2
    demo1_fav1 = Favorite(userId='1', productId='2')
    demo1_fav2 = Favorite(userId='1', productId='3')
    
    # User 2 favorites Product 2 and Product 3
    marnie2_fav1 = Favorite(userId='2', productId='1')
    marnie2_fav2 = Favorite(userId='2', productId='3')
    
    # User 3 favorites Product 1, Product 2, and Product 3
    bobbie3_fav1 = Favorite(userId='3', productId='1')
    bobbie3_fav2 = Favorite(userId='3', productId='2')

    db.session.add(demo1_fav1)
    db.session.add(demo1_fav2)
    db.session.add(marnie2_fav1)
    db.session.add(marnie2_fav2)
    db.session.add(bobbie3_fav1)
    db.session.add(bobbie3_fav2)

    db.session.commit()

def undo_favorites():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.favorites RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM favorites"))
        
    db.session.commit()

    