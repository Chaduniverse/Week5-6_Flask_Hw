from flask import render_template, request,flash, redirect, url_for
from app.blueprints.posts.forms import PokemonForm
from app.blueprints.posts import posts
from app.models import Pokemon
from flask_login import login_required, current_user


@posts.route('/catch_pokemon',methods = ['GET','POST'])
@login_required  
def catch_pokemon():
    form = PokemonForm()
    if request.method == 'POST' and form.validate_on_submit():
        
        # grabbing our form data and storing into a dict  

        new_pokemon_data = {
            'image_url':form.image_url.data,
            'name':form.name.data,
            'ability': form.ability.data,
            'base_stat_hp':form.base_stat_hp.data,
            'base_stat_defense':form.base_stat_defense.data,
            'user_id': current_user.id

        }  

        #create instance of post  
        new_pokemon = Pokemon()  

        # implementing form values from our form data for our instance  

        new_pokemon.from_dict(new_pokemon_data)   

        #save our database  

        new_pokemon.save_to_db()
        flash('You have successfully caught a pokemon!','success')
        return redirect(url_for('posts.view_pokemon')) 
    return render_template('catch_pokemon.html',form=form)  


#view all posts  
@posts.route('/view_pokemon', methods=['GET'])
def view_pokemon():
    posts= Pokemon.query.all()
   
    return render_template('view_pokemon.html', posts=posts)  



