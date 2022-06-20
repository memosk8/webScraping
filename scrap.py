import requests
from bs4 import BeautifulSoup

# solicitud
markup = requests.get(f'https://quotes.toscrape.com/').text

# objeto de tipo beautifulsoup
soup = BeautifulSoup(markup, 'html.parser')
# print(soup.prettify()) #imuestra el html completo

# for item in soup.select('.quote'):
#     print(item.get_text())

# print(soup.select_one('.next > a'))

# arreglo de quotes
quotes = []

for item in soup.select('.quote'):
    quote = {}
    quote['text'] = item.select_one('.text').get_text()
    quote['author'] = item.select_one('.author').get_text()
    tags = item.select_one('.tags')
    quote['tags'] = [tag.get_text() for tag in tags.select('.tag')]
    quotes.append(quote)

print(quotes)
