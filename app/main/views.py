from flask import render_template,redirect,url_for,request
from . import main
from ..models import Sources
from ..requests import get_sources,get_articles

@main.route('/')
def index():
    sources = get_sources()
    print (sources)
    
    
    