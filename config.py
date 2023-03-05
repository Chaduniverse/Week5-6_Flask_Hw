import os 

# config section
class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    REGISTERED_USERS = {
    'dylank@thieves.com':{
    'name':'dylan',
    'password':'ilovemydog'
    },
    'christiana@thieves.com':{
    'name':'christian',
    'password':'test123'
    }
}