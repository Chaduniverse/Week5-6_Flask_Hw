from flask import render_template, request 
import requests  
from app.forms import LoginForm
from app import app 
from app.forms import Pick_Pokemon


# routes section
@app.route('/')
def home():
    return render_template('home.html')  

@app.route('/login',methods = ['GET','POST'])  
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data.lower()
        password = form.password.data
        if email in app.config.get('REGISTERED_USERS') and password == app.config.get('REGISTERED_USERS').get(email).get('password'):
            return f"Successfully logged in! Hello,{app.config.get('REGISTERED_USERS').get(email).get('name')}"
        else: 
            error = ('Invalid email or password.')
            return error
    return render_template('login.html',form =form)


@app.route('/pokemon',methods=['GET','POST']) 
def pokemon():
    form = Pick_Pokemon()
    pokemon_info={} 
    if request.method == 'POST':
        pokemon_name = form.name.data.lower()
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
            return error
    return render_template('pokemon.html', form=form) 


