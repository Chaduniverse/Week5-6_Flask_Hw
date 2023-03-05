from flask import Flask, render_template, request 
import requests        
import os
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    REGISTERED_USERS = {
    'dylank@thieves.com':{
    'name':'dylan',
    'password':'ilovemydog'
    },
    'christiana@thieves.com':{
    'name':'christian',
    'password':'test123'
    }
}

class LoginForm(FlaskForm):
    email = EmailField('Email:', validators=[DataRequired()])  
    password = PasswordField('Password:', validators=[DataRequired()])
    submit_btn = SubmitField('Login')


app = Flask(__name__)  
app.config.from_object(Config)





@app.route('/')
def home():
    return render_template('home.html')  

@app.route('/login',methods = ['GET','POST'])  
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = request.form.get('email').lower()
        password = request.form.get('password')
        if email in app.config.get('REGISTERED_USERS') and password == app.config.get('REGISTERED_USERS').get(email).get('password'):
            return f"Successfully logged in! Hello,{app.config.get('REGISTERED_USERS').get(email).get('name')}"
        else: 
            error = 'Invalid email or password.'
            return render_template('login.html', error=error)
    return render_template('login.html',form=form)


@app.route('/pokemon',methods=['GET','POST']) 
def pokemon():
    print(request.method)
    pokemon_info={} 
    if request.method == 'POST':
        pokemon_name = request.form.get('name')
        pokemon_url = request.form.get('pokemon_url')
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'  
        response = requests.get(url)  
        
        if response.ok:
            data=response.json()
            pokemon_info= {
                            'name':data['forms'][0]['name'],
                            'ability':data['abilities'][0]['ability'],
                            'base_stats_hp':data['stats'][0]['base_stat'],
                            'base_stat_defense':data['stats'][2]['base_stat'],  
                            'sprites':data['sprites']['front_shiny']
                          }
            
            return pokemon_info
    
        else:
            error = ('This is an invalid option')
            return render_template('pokemon.html',error=error)
    return render_template('pokemon.html', pokemon_info=pokemon_info) 


