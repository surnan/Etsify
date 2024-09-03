from app.models import db, Order, OrderProduct, Product, User, environment, SCHEMA
from sqlalchemy.sql import text


def seed_orders():
    # Assuming users and products have already been seeded
    user2 = User.query.filter_by(username='marnie').first()
    product1 = Product.query.filter_by(name='Product 1').first()
    product3 = Product.query.filter_by(name='Product 3').first()

    order = Order(user_id=user2.id)
    db.session.add(order)
    db.session.commit()

    order_product1 = OrderProduct(order_id=order.id, product_id=product1.id, quantity=2)
    order_product2 = OrderProduct(order_id=order.id, product_id=product3.id, quantity=1)

    db.session.add(order_product1)
    db.session.add(order_product2)
    db.session.commit()


def undo_orders():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.order_products RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.orders RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM order_products"))
        db.session.execute(text("DELETE FROM orders"))
        
    db.session.commit()
