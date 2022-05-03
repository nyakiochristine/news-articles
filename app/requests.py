from config import config
import urllib.request,json
from .models import Sources,Articles

#get api key
apiKey= None


api_key = config.NEWS_API_KEY
base_url = config.SOURCES_BASE_URL
articles_url = config.ARTICLES_BASE_URL


def get_sources():
    '''
    getting json respo to urllib.request
    '''
    with urllib.request.urlopen(get_sources_url) as url:
            get_sources_data =url.read()
            get_sources_response = json.loads(get_sources_data)
            
            sources_results= None
            
           # if get_sources_response['sources ']