import requests
from bs4 import BeautifulSoup
answer = requests.get('https://ru.wiktionary.org/wiki/' + input().lower())
soup = BeautifulSoup(answer.text, 'html.parser')
print(soup.find('ol').find('li').text)
