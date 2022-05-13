import os

SOURCES_BASE_URL='http://newsapi.org/v2/sources?apikey='
ARTICLES_BASE_URL='http://newsapi.org/v2/everything?domains=wsj.com,nytimes.com&apiKey='
API_KEY= os.environ.get('API_KEY')

@staticmethod
def init_app(app):
        pass

class Config:
    '''
    general configuration class
    '''


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
    
}
    