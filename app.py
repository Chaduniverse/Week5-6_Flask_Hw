from flask import Flask, render_template, request 
import requests

app = Flask(__name__)  

@app.route('/')
def home():
    return render_template('home.html')  

@app.route('/pokemon',methods=['GET','POST']) 
def pokemon(pokemon_name):
    print(request.method)
    pokemon_info={} 
    if request.method == 'POST':
        pokemon_name = request.form.get('name')
        pokemon_url = request.form.get('pokemon_url')
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'  
        response = requests.get(url)  
        
        if response.ok:
            name = response.json()['forms'][0]['name']
            pokemon_info['name']=name  
            ability=response.json()['abilities'][0]['ability']
            pokemon_info['ability']= ability  
            base_stats_hp= response.json()['stats'][0]['base_stat']
            pokemon_info['base_stat_hp']= base_stats_hp 
            base_stat_attack= response.json()['stats'][1]['base_stat']
            pokemon_info['base_stat_attack']= base_stat_attack  
            base_stat_defense= response.json()['stats'][2]['base_stat']
            pokemon_info['base_stat_defense']= base_stat_defense 
            sprites=response.json()['sprites']['front_shiny']
            pokemon_info['sprites']= sprites 

            return pokemon_info
              
        else:
            return 'This is an invalid option'
    return render_template('pokemon.html', pokemon_info=pokemon_info) 
