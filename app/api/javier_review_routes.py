# from flask import Blueprint, request, jsonify
# from flask_login import login_required, current_user
# from app.models import db, ShoppingCart, CartProduct, Product, Review

# review_productID_bp = Blueprint('review_productID', __name__)

# #Get Reviews per Product Id
# @review_productID_bp.route('/<int:product_id>', methods=['GET'])
# def get_reviews(product_id):
#     # Grab/Query Review by product_id
#     reviews = Review.query.filter_by(productId=product_id).all()

#     # Return the reviews as a list of dictionaries
#     return jsonify([review.to_dict() for review in reviews]), 200

# #Delete Reviews
# @review_productID_bp.route('/<int:id>', methods=['DELETE'])
# def delete_review(id):
#     # Grab/Query Review by id
#     review = Review.query.get(id)

#     # If the review does not exist, return a 404 error
#     if not review:
#         return jsonify({'error': 'Review not found'}), 404

#     # Delete Review
#     db.session.delete(review)
#     db.session.commit()

#     # Return a success message
#     return jsonify({'message': 'Review deleted successfully'}), 200