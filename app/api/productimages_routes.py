# api/productimages_routes.py
from flask import Blueprint, jsonify, redirect, render_template, request


from app.models import db, ProductImage

productimage_routes = Blueprint('productimages', __name__)


# Get All Products
@productimage_routes.route('/', methods=['GET'])
def get_all_products():
    all_products = ProductImage.query.all()
    print("all_products = ", all_products)
    return render_template('productimage_page.html', all_products=all_products)

@productimage_routes.route('/<int:tempId>', methods=['GET'])
def get_productImage_for_product(tempId):
    # Retrieve all product images that match the given productId
    all_product_images = ProductImage.query.filter_by(productId=tempId).all()
    return render_template('productimage_page.html', all_productImages=all_product_images)


# # Get Details of a Specific product
# @productimage_routes.route('/<int:tempId>', methods=['GET'])
# def get_productImage_for_product(tempId):
#     # all_products = ProductImage.query.get(productId=productId)
#     all_products = ProductImage.query.filter_by(productId=tempId)

#     print("tempId - ", tempId)
#     print("===")
#     print("===")
#     print("ALL-PRODUCTS = ", all_products)
#     print("===")
#     print("===")



#     return render_template('productimage_page.html', all_productImages=[all_products])

