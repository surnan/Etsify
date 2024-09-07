from flask import Blueprint, jsonify
from app.models import db, Product

product_routes = Blueprint('products', __name__)


# Get All Products
@product_routes.route('/api/products/all', methods=['GET'])
def get_all_products():
    return jsonify({"products": "hello world!!"}), 200


# Get Details of a Specific product
@product_routes.route('/api/product/<int:productId>', methods=['GET'])
def get_one_product_details(productId):
    return jsonify({"productId": "hello world -ID-"}), 200