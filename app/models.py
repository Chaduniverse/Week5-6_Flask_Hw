from app import db, login 
from flask_login import UserMixin  #only use in your User Class
from datetime import datetime  
from werkzeug.security import generate_password_hash, check_password_hash  





team = db.Table('team',
    db.Column('owner_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('captured_pokemon_id', db.Integer, db.ForeignKey('pokemon.id'))
)


    


class User(UserMixin,db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow()) 
    capture = db.relationship('Pokemon', secondary = team, backref = 'owner', lazy = 'dynamic') 

    # catch method
    def catch(self, poke):
        self.capture.append(poke)
        db.session.commit()
    # remove from team method
    def remove_from_team(self, user):
        self.capture.remove(user)
        db.session.commit()
    

    
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
    base_stats_hp= db.Column(db.Integer)
    base_stat_defense = db.Column(db.Integer)  
    sprites= db.Column(db.String)

    

    
# use this method to register our Post attributes   
    def from_dict(self,data):
        self.name = data['name']
        self.ability = data['ability']
        self.base_stats_hp = data['base_stats_hp']  
        self.base_stat_defense = data['base_stat_defense']
        self.sprites = data['sprites']
       
    
    # save to our database  

    def save_to_db(self):  
        db.session.add(self)
        db.session.commit()

# Update our db
    def update_to_db(self):
        db.session.commit()
    # Delete from db
    def delete_pokemon(self):
        db.session.delete(self)
        db.session.commit()

