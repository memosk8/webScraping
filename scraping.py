from bs4 import BeautifulSoup
import requests

html_doc = requests.get('https://tunein.com/radio/music/').text
soup = BeautifulSoup(html_doc, 'lxml')

page_title = soup.title
section_titles = soup.find_all('div','container-title-module__titleHeader___WUX8D')

# obtener secciones completas
main_containers = soup.find_all('div', 'container-items-module__containerItem___OhnxW')
#clases de subelementos de todas las secciones
elements_classes = ['guide-item-module__guideItemTitleMultiLine___ddgqh',
					'numbered-link-module__numberedLinkContainer___EPfHi',
					'link-module__container___vhfuW', 'titles-module__titleText___KQtb_']

sections = []
elements = []
i = 0
# crear un objeto por cada seccion {titulo: [elementos]}
for container in main_containers:
	#titulo de la seccion
	title = section_titles[i]
	#elementos de la seccion
	print(f"#{i} title: {title.text} ")
	for element in elements_classes:
		if(container.find('div',element)):
			elements.append(container.find('div',element))
			print(element)
	i = i + 1

#sections.append({title.text: elements})
#print(sections[i],'\n')
#i = i + 1
# section# = {section_title: section_elements}

# todos los elementos individuales
# content_classes = soup.find_all('div','guide-item-module__guideItemTitleMultiLine___ddgqh guide-item-module__guideItemTitle___nYoaH')
# content_classes.extend(soup.find_all('div','numbered-link-module__infoContainerWrapper___JIB6D'))
# print(len(content_classes))
# content_classes.extend(soup.find_all('div','titles-module__titleText___KQtb_'))
# print(len(content_classes))
# for item in content_classes:
#	print(item.text)

#Get all the links on <a> tags
#for link in soup.find_all('a'):
	#print(link.get('href'))

