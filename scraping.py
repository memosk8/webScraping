from time import sleep
import requests
from bs4 import BeautifulSoup
import pymongo

html = requests.get('https://tunein.com/radio/music/').text
soup = BeautifulSoup(html, 'html.parser')

main_containers = soup.select('.container-items-module__containerItem___OhnxW')
title_class = "container-title-module__titleHeader___WUX8D"
item_class_row = 'gallery-module__item___lU4KU'
item_class_col = 'row guide-item-module__guideItemContainer___I50sj'
item_classes = ['gallery-module__item___lU4KU', 'guide-item-module__guideItemContainer___I50sj',
                'link-module__container___vhfuW', 'numbered-link-module__infoContainerWrapper___JIB6D', ]
count = 0
for item in main_containers:
    count = count + 1
    print(count)
    print("Sección :", item.find('div', title_class).text)
    if(item.find('div', item_class_row)):
        print("Contenido :", item.find('div', item_class_row).text)
    if(item.find('div', item_class_row)):
        print("Contenido :", item.find('div', item_class_col))
    if(item.find('div', 'link-module__container___vhfuW')):
        print("Contenido :", item.find(
            'div', 'link-module__container___vhfuW').text)
    if(item.find('div', 'numbered-link-module__infoContainerWrapper___JIB6D')):
        print("Contenido :", item.find(
            'div', 'numbered-link-module__infoContainerWrapper___JIB6D').text)
    sleep(0.2)
