from flask_wtf import FlaskForm
from markupsafe import Markup
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DateField, SelectField, TextAreaField, Field, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional
from wtforms.widgets import Input, TextArea
from config import GENDER_OPTIONS, HANDLING_MONEY_OPTIONS, POLITIC_OPTIONS, RELIGION_OPTIONS


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email("Please enter a valid email address.")]) 
    password = PasswordField('Passsword', validators=[DataRequired()])
    remember_me = BooleanField('Remeber Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email("Please enter a valid email address."), Length(max=120)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=64)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=64)])
    date_of_birth = DateField('Date of Birth', validators=[DataRequired()])
    gender = SelectField('Gender', choices=GENDER_OPTIONS, validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired(), Length(max=128)])
    submit = SubmitField('Register')

# HTML5 input sliders for weighted preferences
class RangeInput(Input):
    input_type = "range"
    def __call__(self, field: Field, **kwargs: object) -> Markup:
        kwargs.setdefault("min", 1)
        kwargs.setdefault("max", 5)
        kwargs.setdefault("step", 1)
        return super().__call__(field, **kwargs)
    
class RangeField(Field):
    widget = RangeInput()

    def _value(self):
        if self.data is not None:
            return str(self.data)
        else:
            return '3'  # default value for the slider
        
# checkbox fields
class MultiCheckBoxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class ProfileForm(FlaskForm):
    gender_preference = MultiCheckBoxField('Gender Preferences', choices=GENDER_OPTIONS, validators=[Optional()])
    bio = StringField('Bio', widget=TextArea(), validators=[Optional(), Length(max=1000)])
    religion = SelectField('Religion', choices=RELIGION_OPTIONS, validators=[Optional()])
    politics = MultiCheckBoxField('Politics', choices=POLITIC_OPTIONS, validators=[Optional()])
    handling_money = MultiCheckBoxField('Handling Money', choices=HANDLING_MONEY_OPTIONS, validators=[Optional()])
    hygiene = StringField('Hygiene', validators=[Optional()])
    lifestyle_choices = StringField('Lifestyle Choices', validators=[Optional()])
    submit = SubmitField('Update Profile')

class ProfileMatchForm(FlaskForm):
    religion_preference = StringField('Religion Preference', validators=[Optional()])
    religion_weight = RangeField('Religion Weight', validators=[Optional()])
    
    politics_preference = StringField('Politics Preference', validators=[Optional()])
    politics_weight = RangeField('Politics Weight', validators=[Optional()])
    
    handling_money_preference = StringField('Handling Money Preference', validators=[Optional()])
    handling_money_weight = RangeField('Handling Money Weight', validators=[Optional()])
    
    hygiene_preference = StringField('Hygiene Preference', validators=[Optional()])
    hygiene_weight = RangeField('Hygiene Weight', validators=[Optional()])
    
    lifestyle_choices_preference = StringField('Lifestyle Choices Preference', validators=[Optional()])
    lifestyle_choices_weight = RangeField('Lifestyle Choices Weight', validators=[Optional()])
    submit = SubmitField('Update Matches')

