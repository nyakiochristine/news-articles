from config import Config, SOURCES_BASE_URL,ARTICLES_BASE_URL,API_KEY

import urllib.request,json
from .models import Sources,Articles

#get api key
#api_key= None


#api_key = Config.API_KEY
#base_url = Config.SOURCES_BASE_URL
#articles_url = Config.ARTICLES_BASE_URL


def get_sources():
    '''
    getting json respo to urllib.request
    '''
    with urllib.request.urlopen(SOURCES_BASE_URL  +'1d71fbc2597a4dc5ae9f3f4afe384eee') as url:
            get_sources_data =url.read()
            get_sources_response = json.loads(get_sources_data)
            
            sources_results= None
            
            if get_sources_response['sources ']:
                sources_results_list = get_sources_response['sources']
                sources_results = process_resources(sources_results_list)
                
    return sources_results
    
def process_resources(sources_list):
    '''
    Function  that processes the sources list result and transform them to a list of Objects
    Args:
        movie_list: A list of dictionaries that contain source objects details

    Returns :
        sources_results: A list of source objects
    '''
    source_results= []
    
    
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')
        language = source_item.get('language')
        
        
        if url:
            source_object = Sources (id, name, description, url, category, country,language)
            source_results.append(source_object)
            
    return source_results




def get_articles():
    '''
    returns a list of articles objects
    '''
    with urllib.request.urlopen(ARTICLES_BASE_URL+'1d71fbc2597a4dc5ae9f3f4afe384eee') as url:
        articles_results = json.loads(url.read())
        
        
        articles_object = None
        if articles_results['articles']:
            articles_object = articles_results['articles']
            
    return articles_object

def process_articles(articles_list):
    
    articles_object = []
    for article_item in articles_list:
        id=article_item.get['id']
        author=article_item.get['author']
        title=article_item.get['title']
        description=article_item.get['description']
        url=article_item.get['url']
        image=article_item.get['urlToImage']
        date=article_item.get['publishedAt']
        
        if image:
            articles_result = Articles(id,author,title,description,url,image,date)
            articles_object.append(articles_result)	
        return articles_object
		
    
    
