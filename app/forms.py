from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired

# form section
class LoginForm(FlaskForm):
    
    email = EmailField('Email:', validators=[DataRequired()])  
    password = PasswordField('Password:', validators=[DataRequired()])
    submit_btn = SubmitField('Login')  


class Pick_Pokemon(FlaskForm):  
    name = StringField('name', validators=[DataRequired()])
    submit_btn = SubmitField('Select')  

