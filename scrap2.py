import requests
from bs4 import BeautifulSoup
import pymongo

def scrape_quotes():
    more_links = True  # checa si existen mas paginas
    page = 1  # contador
    quotes = []
    while(more_links):
        markup = requests.get(f'https://quotes.toscrape.com/page/{page}').text
        soup = BeautifulSoup(markup, 'html.parser')
        for item in soup.select('.quote'):
            quote = {}
            quote['text'] = item.select_one('.text').get_text()
            quote['author'] = item.select_one('.author').get_text()
            tags = item.select_one('.tags')
            quote['tags'] = [tag.get_text() for tag in tags.select('.tag')]
            quotes.append(quote)
        # checa si existe un siguiente link
        next_link = soup.select_one('.next > a')
        print(f'Numero de pagina {page}')  # numero de pagina
        # verificar si existen mas paginas
        if(next_link):
            page += 1
        else:
            more_links = False
    return quotes

quotes = scrape_quotes()
client = pymongo.MongoClient('mongodb://127.0.0.1')
scrap = client.scrapweb.quotes
try:
    scrap.insert_many(quotes)
    print(f'se insertaron {len(quotes)} citas')
except pymongo.errors.ConnectionFailure as error:
    print(f'an error occurred: Quotes were not stored to db %s', error)

# print(quotes)
