import os
from flask import Flask, render_template, request, session, redirect, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_login import LoginManager
from .models import db, User, Favorite, Review
from .api.user_routes import user_routes
from .api.auth_routes import auth_routes
from .seeds import seed_commands
from .config import Config


app = Flask(__name__, static_folder='../react-vite/dist', static_url_path='/')

# Setup login manager
login = LoginManager(app)
login.login_view = 'auth.unauthorized'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


# Tell flask about our seed commands
app.cli.add_command(seed_commands)

app.config.from_object(Config)
app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(auth_routes, url_prefix='/api/auth')
db.init_app(app)
Migrate(app, db)

# Application Security
CORS(app)


# Since we are deploying with Docker and Flask,
# we won't be using a buildpack when we deploy to Heroku.
# Therefore, we need to make sure that in production any
# request made over http is redirected to https.
# Well.........
@app.before_request
def https_redirect():
    if os.environ.get('FLASK_ENV') == 'production':
        if request.headers.get('X-Forwarded-Proto') == 'http':
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)


@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response


@app.route("/api/docs")
def api_help():
    """
    Returns all API routes and their doc strings
    """
    acceptable_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    route_list = { rule.rule: [[ method for method in rule.methods if method in acceptable_methods ],
                    app.view_functions[rule.endpoint].__doc__ ]
                    for rule in app.url_map.iter_rules() if rule.endpoint != 'static' }
    return route_list


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def react_root(path):
    """
    This route will direct to the public directory in our
    react builds in the production environment for favicon
    or index.html requests
    """
    if path == 'favicon.ico':
        return app.send_from_directory('public', 'favicon.ico')
    return app.send_static_file('index.html')

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

# Favorites Create Read Delete
# Favorite Create
@app.route('/api/favorites/', methods=['POST'])
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
@app.route('/api/favorites/<int:user_id>', methods=['GET'])
def get_favorites(user_id):
    #Grab/Query Favorites by user
    favorites = Favorite.query.filter_by(user_id=user_id).all()
    #Return Favorites
    return jsonify([favorite.to_dict() for favorite in favorites]), 200

# Favorite Delete
@app.route('/api/favorites/<int:id>', methods=['DELETE'])
def delete_favorite(id):
    #Grab/Query Favorite by the Favorite's id
    favorite = Favorite.query.get(id)

    if not favorite:
        return jsonify({'error': 'Favorite not found'}), 404

    #Delete favorite
    db.session.delete(favorite)
    db.session.commit()

    return jsonify({'message': 'Favorite deleted successfully'}), 200

#Reviews CRUD
#Read (GET) Reviews
@app.route('/api/reviews/<int:product_id>', methods=['GET'])
def get_reviews(product_id):
    # Grab/Query Review by product_id
    reviews = Review.query.filter_by(productId=product_id).all()

    # Return the reviews as a list of dictionaries
    return jsonify([review.to_dict() for review in reviews]), 200

#Delete Reviews
@app.route('/api/reviews/<int:id>', methods=['DELETE'])
def delete_review(id):
    # Grab/Query Review by id
    review = Review.query.get(id)

    # If the review does not exist, return a 404 error
    if not review:
        return jsonify({'error': 'Review not found'}), 404

    # Delete Review
    db.session.delete(review)
    db.session.commit()

    # Return a success message
    return jsonify({'message': 'Review deleted successfully'}), 200