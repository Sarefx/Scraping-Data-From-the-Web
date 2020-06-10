from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://treehouse-projects.github.io/horse-land/index.html')
soup = BeautifulSoup(html.read(), 'html.parser')

divs = soup.find_all('div')  # pulls all div tags
for div in divs:
    print(div)

div = soup.find('div', {'class':'featured'})  # pulls div tags with class featured
print(div)

featured_header = soup.find('div', {'class':'featured'}).h2
print(featured_header.get_text())

for button in soup.find(attrs={'class':'button button--primary'}):
    print(button)

for button in soup.find(class_=button button--primary):  # same as the line above
    print(button)

for link in soup.find_all('a'):
    print(link.get('href'))

