from app.models import db, ShoppingCart, CartProduct, Product, User, environment, SCHEMA
from sqlalchemy.sql import text


def seed_shopping_carts():
    # Assuming users and products have already been seeded
    user1 = User.query.filter_by(username='Demo').first()
    product1 = Product.query.filter_by(name='Product 1').first()
    product2 = Product.query.filter_by(name='Product 2').first()

    # Check if user and products exist
    if not user1:
        print("Error: User 'Demo' not found. Ensure the user has been seeded correctly.")
        return
    if not product1:
        print("Error: Product 'Product 1' not found. Ensure the product has been seeded correctly.")
        return
    if not product2:
        print("Error: Product 'Product 2' not found. Ensure the product has been seeded correctly.")
        return
    

    shopping_cart = ShoppingCart(userId=user1.id)
    db.session.add(shopping_cart)
    db.session.commit()
    
    
    # cart_product1 = CartProduct(shopping_cart_id=shopping_cart.id, product_id=product1.id, quantity=2)
    # cart_product2 = CartProduct(shopping_cart_id=shopping_cart.id, product_id=product2.id, quantity=1)

    cart_product1 = CartProduct(shoppingCartId=shopping_cart.id, productId=product1.id)
    cart_product2 = CartProduct(shoppingCartId=shopping_cart.id, productId=product2.id)
    db.session.add(cart_product1)
    db.session.add(cart_product2)
    db.session.commit()



def undo_shopping_carts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.cartproducts RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.shoppingcarts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM cartproducts"))
        db.session.execute(text("DELETE FROM shoppingcarts"))
        
    db.session.commit()
