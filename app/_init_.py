from flask import Flask
from app import app





def create_app(config_name):
    app = Flask( __name__,config_name=config_name)
    
    
config.from_object(DevConfig)
config.from_pyfile('config.py')


    
from app import views