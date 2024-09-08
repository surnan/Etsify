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
    print('new_review ', new_review)
    print('new_review id ', new_review.id)
    print('new_review stars ', new_review.stars)
    print('new_review userId ', new_review.userId)
    print('new_review productId', new_review.productId)

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
    

#test comment