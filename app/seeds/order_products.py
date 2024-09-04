from app.models import db, OrderProduct, environment, SCHEMA
from sqlalchemy.sql import text

def seed_order_products():
    order_product1 = OrderProduct(
        orderId=1, 
        productId=1, 
        # created_at=??
    )
    order_product2 = OrderProduct(
        orderId=1, 
        productId=2, 
    )
    order_product3 = OrderProduct(
        orderId=2, 
        productId=3, 
    )

    db.session.add(order_product1)
    db.session.add(order_product2)
    db.session.add(order_product3)
    db.session.commit()

def undo_order_products():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.order_products RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM order_products"))
        
    db.session.commit()