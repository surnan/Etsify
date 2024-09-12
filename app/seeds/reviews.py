from app.models import db, Review, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_reviews():
    rev1 = Review(
    stars=5, review='Great concise instructions for how to use', userId=1, productId=1)
    rev2 = Review(
        stars=5, review='Amazing', userId=1, productId=2)
    rev3 = Review(
        stars=5, review='Cozy and Nice', userId=1, productId=3)
    rev4 = Review(
        stars=5, review='Great product', userId=1, productId=4)
    rev5 = Review(
        stars=5, review='Beautiful design and comfortable', userId=1, productId=5)
    rev6 = Review(
        stars=4, review='Nicely built but could use more features', userId=1, productId=6)
    rev7 = Review(
        stars=5, review='Elegant and useful', userId=1, productId=7)
    rev8 = Review(
        stars=5, review='Stunning quality!', userId=1, productId=8)
    rev9 = Review(
        stars=4, review='Looks good, but a bit pricey', userId=1, productId=9)
    rev10 = Review(
        stars=5, review='Best purchase I’ve made recently', userId=1, productId=10)
    rev11 = Review(
        stars=5, review='Beautiful and ornate', userId=2, productId=1)
    rev12 = Review(
        stars=5, review='Aesthetically amazing', userId=2, productId=2)
    rev13 = Review(
        stars=5, review='Intricate and nicely decorated', userId=2, productId=3)
    rev14 = Review(
        stars=5, review='Efficient and easy to figure out how to use', userId=2, productId=4)
    rev15 = Review(
        stars=5, review='Beautifully decorated and easy to use', userId=2, productId=5)
    rev16 = Review(
        stars=4, review='Great for the price', userId=2, productId=6)
    rev17 = Review(
        stars=5, review='Sturdy and well-made', userId=2, productId=7)
    rev18 = Review(
        stars=5, review='High quality materials, love it', userId=2, productId=8)
    rev19 = Review(
        stars=5, review='Sleek and modern design', userId=2, productId=9)
    rev20 = Review(
        stars=5, review='Works perfectly, no issues', userId=2, productId=10)
    rev21 = Review(
        stars=5, review='Outstanding craftsmanship!', userId=3, productId=1)
    rev22 = Review(
        stars=5, review='Perfectly matches the description', userId=3, productId=2)
    rev23 = Review(
        stars=5, review='Cozy and comfortable, highly recommend', userId=3, productId=3)
    rev24 = Review(
        stars=4, review='Great for the price, but could be more durable', userId=3, productId=4)
    rev25 = Review(
        stars=5, review='Excellent quality, very happy', userId=3, productId=5)
    rev26 = Review(
        stars=5, review='Beautiful and works flawlessly', userId=3, productId=6)
    rev27 = Review(
        stars=5, review='Elegant design, very useful', userId=3, productId=7)
    rev28 = Review(
        stars=5, review='Top-notch quality', userId=3, productId=8)
    rev29 = Review(
        stars=4, review='Good, but expected more for the price', userId=3, productId=9)
    rev30 = Review(
        stars=5, review='Works exactly as expected, love it!', userId=3, productId=10)

    

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
    db.session.add(rev11)
    db.session.add(rev12)
    db.session.add(rev13)
    db.session.add(rev14)
    db.session.add(rev15)
    db.session.add(rev16)
    db.session.add(rev17)
    db.session.add(rev18)
    db.session.add(rev19)
    db.session.add(rev20)
    db.session.add(rev21)
    db.session.add(rev22)
    db.session.add(rev23)
    db.session.add(rev24)
    db.session.add(rev25)
    db.session.add(rev26)
    db.session.add(rev27)
    db.session.add(rev28)
    db.session.add(rev29)
    db.session.add(rev30)
    db.session.commit()

def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))
        
    db.session.commit()