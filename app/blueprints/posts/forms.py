from flask_wtf import FlaskForm
from wtforms import  SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired


class PokemonForm(FlaskForm):  
    name= StringField('Name:', validators=[DataRequired()])  
    ability = IntegerField('Ability:', validators=[DataRequired()])
    base_stat_hp= IntegerField('Base Stat hp:', validators=[DataRequired()])  
    base_stat_defense = IntegerField('Base Stat Defense:', validators=[DataRequired()])
    image_url = StringField('Image:', validators=[DataRequired()]) 
    submit_btn = SubmitField('Catch Pokemon!') 

    
    