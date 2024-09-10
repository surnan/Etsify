from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.models import db, ShoppingCart, CartProduct, Product, Review, Favorite

favorite_bp = Blueprint('reviews', __name__)

# Favorites Create Read Delete
# Favorite Create
@favorite_bp.route('/favorites', methods=['POST'])
def create_favorite():
    data = request.get_json() #grab request data
    user_id = data.get('user_id') #grab user_id from req
    product_id = data.get('product_id') #grab product_id from req

    if not user_id or not product_id:
        return jsonify({'error': 'Missing user_id or product_id'}), 400

    #Create Favorite using class
    new_favorite = Favorite(user_id=user_id, product_id=product_id)
    #Add Favorite
    db.session.add(new_favorite)
    db.session.commit()

    return jsonify(new_favorite.to_dict()), 201

# Favorite Read
@favorite_bp.route('/api/favorites/<int:user_id>', methods=['GET'])
def get_favorites(user_id):
    #Grab/Query Favorites by user
    favorites = Favorite.query.filter_by(user_id=user_id).all()
    #Return Favorites
    return jsonify([favorite.to_dict() for favorite in favorites]), 200

# Favorite Delete
@favorite_bp.route('/api/favorites/<int:id>', methods=['DELETE'])
def delete_favorite(id):
    #Grab/Query Favorite by the Favorite's id
    favorite = Favorite.query.get(id)

    if not favorite:
        return jsonify({'error': 'Favorite not found'}), 404

    #Delete favorite
    db.session.delete(favorite)
    db.session.commit()

    return jsonify({'message': 'Favorite deleted successfully'}), 200