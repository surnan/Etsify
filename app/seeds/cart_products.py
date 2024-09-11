from app.models import db, CartProduct, ShoppingCart, Product, environment, SCHEMA
from sqlalchemy.sql import text


def seed_cart_products():
    # Retrieve shopping carts by user ID or another identifiable field
    shopping_cart1 = ShoppingCart.query.filter_by(userId=1).first()  # Adjust as needed
    shopping_cart2 = ShoppingCart.query.filter_by(userId=2).first()  # Adjust as needed

    # Retrieve products by name or another identifiable field
    product1 = Product.query.get(1)  # Adjust to fetch by a reliable attribute
    product2 = Product.query.get(2)
    product3 = Product.query.get(3)

    # Check if all required shopping carts and products exist
    if not shopping_cart1 or not shopping_cart2:
        print("Error: One or more shopping carts not found. Ensure shopping carts are seeded correctly.")
        return
    if not product1 or not product2 or not product3:
        print("Error: One or more products not found. Ensure products are seeded correctly.")
        return

    # Create cart products with valid references
    cart_product1 = CartProduct(
        shoppingCartId=shopping_cart1.id,
        productId=product1.id
    )
    cart_product2 = CartProduct(
        shoppingCartId=shopping_cart1.id,
        productId=product2.id
    )
    cart_product3 = CartProduct(
        shoppingCartId=shopping_cart2.id,
        productId=product3.id
    )

    db.session.add(cart_product1)
    db.session.add(cart_product2)
    db.session.add(cart_product3)
    db.session.commit()

def undo_cart_products():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.cartproducts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM cartproducts"))
        
    db.session.commit()





# def seed_cart_products():
# from app.models import db, CartProduct, environment, SCHEMA
# from sqlalchemy.sql import text
#     # a = 5
#     cart_product1 = CartProduct(
#         shoppingCartId=1, 
#         productId=1
#     )
#     cart_product2 = CartProduct(
#         shoppingCartId=1, 
#         productId=2
#     )
#     cart_product3 = CartProduct(
#         shoppingCartId=2, 
#         productId=3
#     )

#     db.session.add(cart_product1)
#     db.session.add(cart_product2)
#     db.session.add(cart_product3)
#     db.session.commit()

# def undo_cart_products():
#     if environment == "production":
#         db.session.execute(f"TRUNCATE table {SCHEMA}.cart_products RESTART IDENTITY CASCADE;")
#     else:
#         db.session.execute(text("DELETE FROM cart_products"))
        
#     db.session.commit()

# def undo_cart_products():
#     if environment == "production":
#         db.session.execute(f"TRUNCATE table {SCHEMA}.cartproducts RESTART IDENTITY CASCADE;")
#     else:
#         db.session.execute(text("DELETE FROM cartproducts"))
        
#     db.session.commit()