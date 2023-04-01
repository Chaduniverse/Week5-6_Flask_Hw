from flask import render_template, request,redirect,url_for, flash
import requests
from app.blueprints.main import main 
from app.blueprints.auth.forms import Pick_Pokemon 
from flask_login import login_required, current_user 
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
     
    if request.method == 'POST' and form.validate_on_submit():
        pokemon_name = form.name.data.lower()
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'  
        response = requests.get(url)  
        
        if response.ok:
            data=response.json()
            pokedata = []
            pokemon_info= {
                            'name':data['forms'][0]['name'],
                            'ability':data['abilities'][0]['ability']['name'],
                            'base_stats_hp':data['stats'][0]['base_stat'],
                            'base_stat_defense':data['stats'][2]['base_stat'],  
                            'sprites':data['sprites']['front_shiny']
                          }
            for pokemon in current_user.capture:
                if pokemon.name == pokemon_info['name']:
                    flash(f'That pokemon is already on your team! Please choose another.', 'danger')
                    return redirect(url_for('main.search_pokemon'))
            pokedata.append(pokemon_info)
            return render_template('pokemon.html', form=form, pokedata=pokedata)
        else: 
            flash('Pokemon does not exist!','danger')   
            return redirect(url_for('main.search_pokemon')) 
    return render_template('pokemon.html', form=form)   


# creating a catch pokemon route  

@main.route('/catch_pokemon/<poke_name>') 
@login_required
def catch_pokemon(poke_name):
    pokemon = Pokemon.query.filter_by(name=poke_name).first()
    if current_user.capture.count() >= 5:
        flash('Your team is full.', 'danger')
        return redirect(url_for('main.search_pokemon'))
    elif pokemon:
        current_user.catch(pokemon)
        flash(f'Congrats! You have captured a {poke_name.title()}!','success')  
        return redirect(url_for('main.search_pokemon'))  
    else:
        pokemon_name = poke_name
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'  
        response = requests.get(url)  
        
        if response.ok:
            data=response.json()
            pokemon_info= {
                            'name':data['forms'][0]['name'],
                            'ability':data['abilities'][0]['ability']['name'],
                            'base_stats_hp':data['stats'][0]['base_stat'],
                            'base_stat_defense':data['stats'][2]['base_stat'],  
                            'sprites':data['sprites']['front_shiny']
                          } 
            new_pokemon = Pokemon()
            new_pokemon.from_dict(pokemon_info)
            new_pokemon.save_to_db()
            current_user.catch(new_pokemon)  
            flash(f'Congrats! You have captured a {poke_name.title()}!','success')  
            return redirect(url_for('main.search_pokemon'))



    return redirect(url_for('main.search_pokemon'))


@main.route('/view_team') 
@login_required
def view_team():
    my_team = current_user.capture
    return render_template('my_team.html',my_team=my_team) 


@main.route('/battle') 
@login_required
def battle():
    users = User.query.all()
    return render_template('battle.html',users=users) 

        
        
@main.route('/battleroute/<user_id>') 
@login_required
def battleroute(user_id):
    users = User.query.all()
    user = User.query.get(user_id)
    home_team = current_user.capture 
    visiting_team = user.capture
    
    home_health = []
    visiting_health= []

    for health in visiting_team: 
        visiting_health.append(health.base_stats_hp) 
    for health in home_team:
        home_health.append(health.base_stats_hp)
    
    total_home_health= sum(home_health)
    total_visiting_health = sum(visiting_health) 
    
    if total_home_health > total_visiting_health:
        flash(f'You won the Battle!', 'success')  
    else:
        flash(f'You lost the Battle!', 'danger')
    return render_template('battle.html', users=users) 

               