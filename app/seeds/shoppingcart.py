from app.models import db, ShoppingCart, CartProduct, Product, User, environment, SCHEMA
from sqlalchemy.sql import text


def seed_shopping_carts():
    # Assuming users and products have already been seeded
    user1 = User.query.filter_by(username='Demo').first()
    user2 = User.query.filter_by(username='marnie').first()
    
    # product1 = Product.query.filter_by(name='Product 1').first()
    # product2 = Product.query.filter_by(name='Product 2').first()

    shopping_cart1 = ShoppingCart(userId=user1.id)
    shopping_cart2 = ShoppingCart(userId=user2.id)
    db.session.add(shopping_cart1)
    db.session.add(shopping_cart2)
    db.session.commit()

    # cart_product1 = CartProduct(shoppingCartId=shopping_cart.id, productId=product1.id)
    # cart_product2 = CartProduct(shoppingCartId=shopping_cart.id, productId=product2.id)
    # db.session.add(cart_product1)
    # db.session.add(cart_product2)
    # db.session.commit()

def undo_shopping_carts():
    if environment == "production":
        # db.session.execute(f"TRUNCATE table {SCHEMA}.cartproducts RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.shoppingcarts RESTART IDENTITY CASCADE;")
    else:
        # db.session.execute(text("DELETE FROM cartproducts"))
        db.session.execute(text("DELETE FROM shoppingcarts"))
        
    db.session.commit()
