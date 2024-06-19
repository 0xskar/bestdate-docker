from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email
from wtforms.fields import EmailField


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email("Please enter a valid email address.")]) 
    password = PasswordField('Passsword', validators=[DataRequired()])
    remember_me = BooleanField('Remeber Me')
    submit = SubmitField('Sign In')
