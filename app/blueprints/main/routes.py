from flask import render_template, request
import requests
from app.blueprints.main import main 
from app.blueprints.auth.forms import Pick_Pokemon 


from flask_login import login_required


# routes section
@main.route('/')
def home():
    return render_template('home.html')  


    

@main.route('/pokemon',methods=['GET','POST']) 
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


