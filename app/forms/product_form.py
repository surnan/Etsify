from flask_wtf import FlaskForm
from wtforms import StringField
from app.models import Product
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
