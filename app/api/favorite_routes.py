from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.models import db, ShoppingCart, CartProduct, Product, Review, Favorite

favorite_bp = Blueprint('favorites', __name__)

# Favorites Create Read Delete
# Favorite Create
@favorite_bp.route('/', methods=['POST'])
def create_favorite():
    data = request.get_json() #grab request data
    userId = data.get('userId') #grab user_id from req
    productId = data.get('productId') #grab product_id from req

    if not userId or not productId:
        return jsonify({'error': 'Missing userId or productId'}), 400

    #Create Favorite using class
    new_favorite = Favorite(userId=userId, productId=productId)
    #Add Favorite
    db.session.add(new_favorite)
    db.session.commit()

    return jsonify(new_favorite.to_dict()), 201

# Favorite Read
@favorite_bp.route('/<int:userId>', methods=['GET'])
def get_favorites(userId):
    #Grab/Query Favorites by user
    favorites = Favorite.query.filter_by(userId=userId).all()
    #Return Favorites
    return jsonify([favorite.to_dict() for favorite in favorites]), 200

# Favorite Delete
@favorite_bp.route('/<int:id>', methods=['DELETE'])
def delete_favorite(id):
    #Grab/Query Favorite by the Favorite's id
    favorite = Favorite.query.get(id)

    if not favorite:
        return jsonify({'error': 'Favorite not found'}), 404

    #Delete favorite
    db.session.delete(favorite)
    db.session.commit()

    return jsonify({'message': 'Favorite deleted successfully'}), 200