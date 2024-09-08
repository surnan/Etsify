# api/product_routes.py
from flask import Blueprint, jsonify, redirect, render_template, request
from app.models import db, Review
review_routes = Blueprint('reviews', __name__)

@review_routes.route('/', methods = ['GET'])
def get_all_reviews():
    all_reviews = Review.query.all()
    return render_template('review_page.html', all_reviews=all_reviews)


@review_routes.route('/', methods=['POST'])
def add_review():
    data = request.get_json()
    stars = data.get("stars")
    review = data.get("review")
    userId = data.get("userId")
    productId = data.get("productId")
    new_review = Review(stars=stars, review=review, userId=userId, productId=productId)
   
    try:
        db.session.add(new_review)
        db.session.commit()
        return jsonify({"message": "Review added successfully", "review": {
            "stars": new_review.stars,
            "review": new_review.review,
            "userId": new_review.userId,
            "productId": new_review.productId
        }})
        # return render_template('review_page.html', all_reviews=[new_review])
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@review_routes.route('/<int:reviewId>', methods=['DELETE'])
def delete_review(reviewId):
    review = Review.query.get(reviewId)

    if not review:
        return jsonify({"error": "Product not found"}), 404
    
    try:
        db.session.delete(review)
        db.session.commit()
        return jsonify({"message": f"Review with ID {reviewId} has been deleted."}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
@review_routes.route('/<int:reviewId>', methods=['PUT'])
def update_review(reviewId):
    review = Review.query.get(reviewId)
    print("The review is, ", review)
    
    if not review:
        return jsonify({"error": "Review not found"}), 404
    data = request.get_json()
    stars = data.get('stars', review.stars)
    review_text = data.get('review', review.review)
    userId = data.get('userId', review.userId)
    productId = data.get('productId', review.productId)

    review.stars = stars
    print('stars ',review.stars)
    review.review = review_text
    print('review ', review.review)
    review.userId = userId
    print('userId ', review.userId)
    review.productId = productId
    print('product ', review.productId)

    # review = {
    #     "stars": stars,
    #     "review": review,
    #     "userId": userId,
    #     "productId":productId
    # }

  
   
    try:
        db.session.commit()
        return jsonify({"message": "Review updated successfully", "review": {
            "id": review.id,
            "stars": review.stars,
            "review": review.review,
            "userId": review.userId,
            "productId": review.productId
        }})
        # return render_template('review_page.html', all_reviews=[new_review])
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500




#test comment