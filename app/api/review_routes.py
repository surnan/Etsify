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

    return render_template('review_page.html', all_reviews=[new_review])

    print("=== NEW_REVIEW ======")
    print(new_review)
    print("=========")
    print("=========")





    try:
        db.session.add(new_review)
        db.commit()
        return jsonify({"message": "Review added successfully", "review": {
            "stars": new_review.stars,
            "review": new_review.review,
            "userId": new_review.userId,
            "productId": new_review.productId
        }})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    

#test comment