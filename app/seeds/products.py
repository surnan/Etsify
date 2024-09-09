from app.models import db, Product, environment, SCHEMA
from sqlalchemy.sql import text

def seed_products():
    product1 = Product(
        sellerId=1, 
        name='Can of beans', 
        description='Beans description', 
        price=1.99, 
        stock=100000,
        # created_at=??
    )
    product2 = Product(
        sellerId=2, 
        name='Vape', 
        description='Vape description', 
        price=29.99, 
        stock=200,
    )
    product3 = Product(
        sellerId=3, 
        name='CyberTruck', 
        description='CyberTruck description', 
        price=60000.99, 
        stock=300,
    )

    db.session.add(product1)
    db.session.add(product2)
    db.session.add(product3)
    db.session.commit()

def undo_products():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.products RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM products"))
        
    db.session.commit()