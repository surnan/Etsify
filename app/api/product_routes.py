# api/product_routes.py
from flask import Blueprint, jsonify
from app.models import db, Product

product_routes = Blueprint('products', __name__)


# Get All Products
@product_routes.route('/', methods=['GET'])
def get_all_products():
    print('Going down route=/api/products')
    return "<h1>Hellow World</h1>"


# Get Details of a Specific product
@product_routes.route('/<int:productId>', methods=['GET'])
def get_one_product_details(productId):
    print('/api/product/<int:productId>')
    return "<h1>Hellow World - ProductId</h1>"