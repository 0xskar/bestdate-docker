from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileSize, FileRequired
from markupsafe import Markup
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DateField, SelectField, TextAreaField, Field, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional
from wtforms.widgets import Input, TextArea
from config import GENDER_OPTIONS, HANDLING_MONEY_OPTIONS, POLITIC_OPTIONS, RELIGION_OPTIONS, SHOWERING_FREQUENCY_OPTIONS, ORAL_CARE_OPTIONS, CIGARETTE_SMOKING_OPTIONS, LIVING_SPACE_CLEANLINESS_OPTIONS, ALCHOHOL_COMSUMPTION_OPTIONS, MARIJUANA_CONSUMPTION_OPTIONS


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

# Profile Customization Form
class ProfileForm(FlaskForm):
    profile_picture = FileField('Profile Picture', validators=[
        Optional(),
        FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!'),
        FileSize(max_size=8 * 1024 * 1024)  # 8 MB
    ])
    bio = StringField('Bio', widget=TextArea(), validators=[Optional(), Length(max=1000)])
    religion = SelectField('Religion', choices=RELIGION_OPTIONS, validators=[Optional()])
    politics = MultiCheckBoxField('Politics', choices=POLITIC_OPTIONS, validators=[Optional()])
    handling_money = MultiCheckBoxField('Handling Money', choices=HANDLING_MONEY_OPTIONS, validators=[Optional()])
    health_living_space_cleanliness = SelectField('How often do you clean house?', choices=LIVING_SPACE_CLEANLINESS_OPTIONS, validators=[Optional()])
    health_showering_frequency = SelectField('Showering Frequency', choices=SHOWERING_FREQUENCY_OPTIONS, validators=[Optional()])
    health_oral_care = SelectField('Oral Care', choices=ORAL_CARE_OPTIONS, validators=[Optional()])
    health_smoking = SelectField('Tobacco smoking', choices=CIGARETTE_SMOKING_OPTIONS, validators=[Optional()])
    health_alchohol_consumption = SelectField('Alchohol', choices=ALCHOHOL_COMSUMPTION_OPTIONS, validators=[Optional()])
    health_marijuana_consumption = SelectField('Marijuana', choices=MARIJUANA_CONSUMPTION_OPTIONS, validators=[Optional()])
    submit = SubmitField('Update Profile')

# Matchmaking selection form
class ProfileMatchForm(FlaskForm):
    gender_preference = MultiCheckBoxField('Gender Preferences', choices=GENDER_OPTIONS, validators=[Optional()])
    religion_preference = StringField('Religion Preference', choices=RELIGION_OPTIONS, validators=[Optional()])
    politics_preference = StringField('Politics Preference', choices=POLITIC_OPTIONS, validators=[Optional()])
    handling_money_preference = StringField('Handling Money Preference', choices=HANDLING_MONEY_OPTIONS, validators=[Optional()])
    health_living_space_cleanliness_preference = SelectField('How often do you clean house?', choices=LIVING_SPACE_CLEANLINESS_OPTIONS, validators=[Optional()])
    health_showering_frequency_preference = SelectField('Showering Frequency', choices=SHOWERING_FREQUENCY_OPTIONS, validators=[Optional()])
    health_oral_care_preference = SelectField('Oral Care', choices=ORAL_CARE_OPTIONS, validators=[Optional()])
    health_smoking_preference = SelectField('Tobacco smoking', choices=CIGARETTE_SMOKING_OPTIONS, validators=[Optional()])
    health_alchohol_consumption_preference = SelectField('Alchohol consumption', choices=ALCHOHOL_COMSUMPTION_OPTIONS, validators=[Optional()])
    health_marijuana_consumption_preference = SelectField('Alchohol consumption', choices=MARIJUANA_CONSUMPTION_OPTIONS, validators=[Optional()])
    submit = SubmitField('Update Matches')

