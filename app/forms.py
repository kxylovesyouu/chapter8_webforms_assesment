from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, EmailField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo


class RegisterForm(FlaskForm):
    """Register Form"""
    username = StringField('Username', validators= [DataRequired(), Length(1, 64)])
    email = EmailField('Email', validators = [DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators= [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators= [DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class AddProductForm(FlaskForm):
    """Add Product Form"""
    product_name = StringField('Product Name',validators= [DataRequired(), Length(1, 64)] )
    product_description = StringField('Product Description', validators= [DataRequired(), Length(1, 64)])
    stock_available = SelectField('Stock Available', choices=[('1', '1'), ('5', '5'), ('12', '12'), ('20', '20') ])
    submit = SubmitField('Add Product')