from bs4 import BeautifulSoup

with open("./fb_eventos.html", 'r') as html_file:
   content = html_file.read()
   # print(content)
   soup = BeautifulSoup(content, 'lxml')
   # print(soup.prettify())
   span_tags = soup.find_all('span')
   
   for spanTag in span_tags:
      print(spanTag.text)
      
