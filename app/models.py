from app import db, login 
from flask_login import UserMixin  #only use in your User Class
from datetime import datetime  
from werkzeug.security import generate_password_hash, check_password_hash  





class Caught_Pokemon(db.Model):  
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, nullable=False)
    ability= db.Column(db.String) 
    image_url= db.Column(db.String)
    base_stat_hp= db.Column(db.Integer)
    base_stat_defense = db.Column(db.Integer)  


    def save_to_db(self):  
        db.session.add(self)
        db.session.commit()


    


class User(UserMixin,db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow()) 
   
    

    
#    Hashes our password
    def hash_password(self,original_password):
        return generate_password_hash(original_password)  
    
# check password hash  
    def check_hash_password(self,login_password):
        return check_password_hash(self.password,login_password)  
    
# use to method to register our user attributes   
    def from_dict(self,data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = self.hash_password(data['password'])  

# save to our database  

    def save_to_db(self):  
        db.session.add(self)
        db.session.commit()


@login.user_loader  
def load_user(user_id):
    return User.query.get(user_id)  

class Pokemon(db.Model):  
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, nullable=False)
    ability= db.Column(db.String) 
    image_url= db.Column(db.String)
    base_stat_hp= db.Column(db.Integer)
    base_stat_defense = db.Column(db.Integer)  

    def check_pokemon(pokemon_name): 
        return Pokemon.query.filter_by(pokemon_name=pokemon_name).first()
        

    
# use this method to register our Post attributes   
    def from_dict(self,data):
        self.image_url = data['image_url']
        self.name = data['name']
        self.ability = data['ability']
        self.base_stat_hp = data['base_stat_hp']  
        self.base_stat_defense = ['base_stat_defense']
       
    
    # save to our database  

    def save_to_db(self):  
        db.session.add(self)
        db.session.commit()



