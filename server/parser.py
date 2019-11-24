from bs4 import BeautifulSoup as bs
import requests
from random import randint
import json
from pymorphy2 import MorphAnalyzer


class Parser:
    def __init__(self):
        self.url = 'https://ru.wiktionary.org/wiki/'
        self.headers = {'accept': '*/*',
                        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
        self.session = requests.Session()
        self.morph = MorphAnalyzer()

    def find(self, content):

        variants = self.morph.parse(content)


        word = variants[0].normal_form

        request = self.session.get(self.url + word.lower())
        soup = bs(request.text, 'html.parser')

        response = soup.find('ol').find('li')

        if response != None:

            response_dict = {
                'text': response.text,
                'title': content
            }

            response_dict['text'] = response_dict['text'].replace('\n', 'dp-trans')
            return json.dumps(response_dict)
        else:
            response_dict = {
                'text': "Информация не найденна(",
                'title': content
            }
            return json.dumps(response_dict)

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

    def parse_current_page_chrome(self, url):
        request = self.session.get(url, headers=self.headers)
        soup = bs(request.text, 'html.parser')
        [s.extract() for s in soup('script')]
        all_words = set(soup.text.replace('\n', ' ').split())

        dialects = {
            'words': []
        }
        processed_words = []
        for word in all_words:
            variants = self.morph.parse(word.replace(',', '').replace('.', '').replace('!', ''))
            processed_words.append(variants[0].normal_form)
        for i in range(5):
            dialects['words'].append(processed_words[randint(0, len(processed_words))])

        print("Send!")
        return json.dumps(dialects)
