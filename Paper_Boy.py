import requests
from sys import argv

API_KEY = '38e33e9b961440a0954bd99c3d1a3520'

URL = ('https://newsapi.org/v2/top-headlines?')


def get_articles_by_category(category):
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": "us",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def get_artciles_by_query(query):
    query_parameters = {
        "q": query,
        "sortBy": "top",
        "country": "us",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def _get_articles(params):
    response = requests.get(URL, params=params)

    articles = response.json()['articles']

    results = []
        
    for article in articles:
        results.append({"title": article["title"], "url": article["url"]})

    for result in results:
        print(result['title'])
        print(result['url'])
        print('')

def get_sources_by_category(category):
    url = 'https://newsapi.org/v2/top-headlines/sources'
    query_parameters = {
        "category": category,
        "language": "en",
        "apiKey": API_KEY
    }

    response = requests.get(url, params=query_parameters)

    sources = response.json()['sources']

    for source in sources:
        print(source['name'])
        print(source['url'])


if __name__ == "__main__":
    print("Hear Ye Hear Ye, Read All About It...\n")
    get_articles_by_category(argv[1])
    print("More News at 6. Back to you in the studio.")
    