from app.models import db, Product, environment, SCHEMA
from sqlalchemy.sql import text

def seed_products():
    product1 = Product(
        sellerId=1, 
        name='Can of beans', 
        description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor ', 
        price=1.99, 
        stock=100000,
    )
    product2 = Product(
        sellerId=2, 
        name='Vape', 
        description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor ', 
        price=29.99, 
        stock=200,
    )
    product3 = Product(
        sellerId=3, 
        name='CyberTruck', 
        description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor ', 
        price=60000.99, 
        stock=300,
    )
    product4 = Product(
        sellerId=1, 
        name='Pikachu', 
        description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor ', 
        price=325.23, 
        stock=400,
    )
    product5 = Product(
        sellerId=2, 
        name='Super Nintendo (SNES)', 
        description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor ', 
        price=465.23, 
        stock=300,
    )
    product6 = Product(
        sellerId=3, 
        name='ELectric Piano', 
        description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor ', 
        price=95.25, 
        stock=300,
    )
    product7 = Product(
        sellerId=3, 
        name='MacBook Pro', 
        description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor ', 
        price=751.05, 
        stock=300,
    )
    product8 = Product(
        sellerId=1, 
        name='Tea Cup', 
        description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor ', 
        price=693.10, 
        stock=300,
    )
    product9 = Product(
        sellerId=2, 
        name='Tropical Collar', 
        description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor ', 
        price=985.45, 
        stock=300,
    )
    product10 = Product(
        sellerId=3, 
        name='Cuban Coffee Cup', 
        description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor ', 
        price=1350.29, 
        stock=300,
    )

    db.session.add(product1)
    db.session.add(product2)
    db.session.add(product3)
    db.session.add(product4)
    db.session.add(product5)
    db.session.add(product6)
    db.session.add(product7)
    db.session.add(product8)
    db.session.add(product9)
    db.session.add(product10)
    db.session.commit()

def undo_products():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.products RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM products"))
        
    db.session.commit()