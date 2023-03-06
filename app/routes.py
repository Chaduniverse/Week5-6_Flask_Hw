from flask import render_template, request,flash, redirect, url_for
import requests  
from app.forms import LoginForm, RegistrationForm
from app import app 
from app.forms import Pick_Pokemon 
from app.models import User


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
            flash(f"Successfully logged in! Hello,{app.config.get('REGISTERED_USERS').get(email).get('name')}",'success')
            return render_template('home.html')
        else: 
            error = ('Invalid email or password.')
            flash(f'{error}','danger')
            return render_template('login.html',form=form)
    return render_template('login.html',form=form)

@app.route('/register',methods = ['GET','POST'])  
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        
        # grabbing our form data and storing into a dict  

        new_user_data = {
            'first_name':form.first_name.data.title(),
            'last_name':form.last_name.data.title(),
            'email': form.email.data.lower(),
            'password': form.password.data

        }  

        #create instance of user  
        new_user =User()  

        # implementing form values from our form data for our instance  

        new_user.from_dict(new_user_data)   

        #save our database  

        new_user.save_to_db()
        return redirect(url_for('login')) 
    return render_template('register.html',form=form)


        

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


