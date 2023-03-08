from flask import Flask
from config import Config 
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# initializing section  

  

# instances of packages 
login = LoginManager()
db = SQLAlchemy()
migrate = Migrate()

def create_app():
# initializing section 
    app = Flask(__name__)
    # link to our config  
    app.config.from_object(Config)  

    #register packages
    login.init_app(app) 
    db.init_app(app)  
    migrate.init_app(app,db) 

    # configure login settings 
    login.login_view ='login'
    login.login_message = 'You must be logged in to view this page.'
    login.login_message_category = 'warning'  

    #importing blueprints 
    from app.blueprints.main import main   
    from app.blueprints.auth import auth

    #registering blueprints
    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app



