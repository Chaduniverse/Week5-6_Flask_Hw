from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired, EqualTo

# form section
class LoginForm(FlaskForm):
    
    email = EmailField('Email:', validators=[DataRequired()])  
    password = PasswordField('Password:', validators=[DataRequired()])
    submit_btn = SubmitField('Login')  


class Pick_Pokemon(FlaskForm):  
    name = StringField('name', validators=[DataRequired()])
    submit_btn = SubmitField('Select')  

class RegistrationForm(FlaskForm):  
    first_name= StringField('First Name:', validators=[DataRequired()])  
    last_name= StringField('Last Name:', validators=[DataRequired()])
    submit_btn = SubmitField('Login')  
    email = EmailField('Email:', validators=[DataRequired()])  
    password = PasswordField('Password:', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password: ',validators=[DataRequired(),EqualTo('password')])
    submit_btn = SubmitField('Signup')  


class EditProfileForm(FlaskForm):
    first_name= StringField('First Name:', validators=[DataRequired()])  
    last_name= StringField('Last Name:', validators=[DataRequired()])
    submit_btn = SubmitField('Login')  
    email = EmailField('Email:', validators=[DataRequired()])  
    submit_btn = SubmitField('Update')  

