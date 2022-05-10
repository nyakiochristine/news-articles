from distutils import config
from flask import Flask
import app
from config import DevConfig





def create_app(config_name):
    app = Flask( __name__,config_name=config_name)
    
    
config.from_object(DevConfig)
config.from_pyfile('config.py')


    
from app import views