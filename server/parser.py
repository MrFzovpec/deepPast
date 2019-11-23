from bs4 import BeautifulSoup as bs
import requests
from random import randint
import json
from pymorphy2 import MorphAnalyzer


class Parser:
    def __init__(self):
        self.url = 'https://gufo.me/dict/ozhegov/'
        self.headers = {'accept': '*/*',
                        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
        self.session = requests.Session()
        self.morph = MorphAnalyzer()

    def find(self, content):

        variants = self.morph.parse(content)


        word = variants[0].normal_form

        request = self.session.get(
            self.url + str(word), headers=self.headers)
        soup = bs(request.text, 'html.parser')

        response = soup.article

        if response != None:
            return response.text
        else:
            return "Информация не найденна("

    def parse_current_page(self, url):
        request = self.session.get(url, headers=self.headers)
        soup = bs(request.text, 'html.parser')
        poems = soup.find_all(attrs={"class": 'dpast__content'})

        dialects = {
            'words': []
        }

        for poem in poems:
            poem = poem.text.replace('  ', "").replace(',', '').replace('!', '').replace('.', '').replace('\n', ' ').split()

            dialects['words'].append(poem[randint(0, len(poem))])

        return json.dumps(dialects)
