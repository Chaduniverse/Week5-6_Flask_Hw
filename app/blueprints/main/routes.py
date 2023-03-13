from flask import render_template, request
import requests
from app.blueprints.main import main 
from app.blueprints.auth.forms import Pick_Pokemon 
from flask_login import login_required 
from ...models import User, Pokemon 


# routes section
@main.route('/')
def home():
    users= User.query.all()
    print(users)
    return render_template('home.html', users=users)  


    

@main.route('/search_pokemon',methods=['GET','POST']) 
@login_required
def search_pokemon():
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
            
            
        if not  Pokemon.check_pokemon(pokemon_info['name']):
            new_pokemon = Pokemon()
            new_pokemon.from_dict(pokemon_info)
            new_pokemon.save_to_db()
            return new_pokemon
            

            
           
    
        else:
            error = ('This is an invalid option')
            return error
    return render_template('pokemon.html', form=form)   


# creating a catch pokemon route  


        
        
        