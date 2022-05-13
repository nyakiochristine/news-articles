from flask import render_template, redirect,request,url_for
from . import main
from ..models import Sources
from ..requests import get_sources,get_articles

@main.route('/')
def index():
    source = get_sources
    print (source)

    title = 'Home - Some of the best news sources'
    return render_template('index.html', title = title, source = source)

@main.route('/news')
def news():
    
    '''
    Views the news page functionality that returns newshighlightd details and its data
    
    '''
    articles = get_articles()
    title = 'Articles - Some of the articles'
    return render_template('news.html', articles=articles, title = title)
    
    