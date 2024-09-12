from app.models import db, CartProduct, environment, SCHEMA
from sqlalchemy.sql import text

def seed_cart_products():
    # a = 5
    cart_product1 = CartProduct(
        shoppingCartId=1, 
        productId=1
    )
    cart_product2 = CartProduct(
        shoppingCartId=1, 
        productId=2
    )
    cart_product3 = CartProduct(
        shoppingCartId=2, 
        productId=3
    )

    db.session.add(cart_product1)
    db.session.add(cart_product2)
    db.session.add(cart_product3)
    db.session.commit()

def undo_cart_products():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.cart_products RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM cart_products"))
        
    db.session.commit()

def undo_cart_products():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.cartproducts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM cartproducts"))
        
    db.session.commit()