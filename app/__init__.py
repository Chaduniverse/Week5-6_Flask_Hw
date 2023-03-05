from flask import Flask
from config import Config

# initializing section  
app = Flask(__name__)  
app.config.from_object(Config) 
from app import routes