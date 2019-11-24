from bs4 import BeautifulSoup as bs
import requests
from random import randint
import json
from pymorphy2 import MorphAnalyzer
from nltk.tokenize import TweetTokenizer
from pymorphy2 import MorphAnalyzer
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')


class Parser:
    def __init__(self):
        self.url = 'https://ru.wiktionary.org/wiki/'
        self.headers = {'accept': '*/*',
                        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
        self.session = requests.Session()
        self.morph = MorphAnalyzer()
        text = open('olds.json', 'r').read()
        self.olds = json.loads(text)

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

            response_dict['text'] = response_dict['text'].replace(
                '\n', 'dp-trans')
            return json.dumps(response_dict)
        else:
            response_dict = {
                'text': "Информация не найденна(",
                'title': content
            }
            return json.dumps(response_dict)

    def parse_current_page(self, url):
        word_dict = {}
        request = self.session.get(url, headers=self.headers)
        soup = bs(request.text, 'html.parser')
        poems = soup.find_all(attrs={"class": 'dpast__content'})

        dialects = {
            'words': []
        }

        def superrost(words):
            return ''.join(filter(lambda x: ord(x) in range(ord('а'), ord('я') + 1) or
                                  ord(x) in range(ord('А'), ord('Я') + 1) or
                                  x == ' ', list(words.replace('\\n', ' '))))

        tokenizer = TweetTokenizer()
        analyzer = MorphAnalyzer()

        def preprocess(text):
            w = text.lower().split()

            filtered_words = [
                word for word in w if word not in stopwords.words('russian')]

            words = tokenizer.tokenize(' '.join(filtered_words))

            for i in range(len(words)):
                k = analyzer.parse(words[i])[0].normal_form
                word_dict[k] = words[i]
                words[i] = k
            return ' '.join(words)

        for poem in poems:
            poem = poem.text
            poem = preprocess(superrost(poem)).split()


            for w in poem:
                if w in self.olds:
                    dialects['words'].append(word_dict[w])
        return json.dumps(dialects)

    def parse_current_page_chrome(self, url):
        request = self.session.get(url, headers=self.headers)
        soup = bs(request.text, 'html.parser')
        [s.extract() for s in soup('script')]
        text = soup.text

        word_dict = {}

        dialects = {
            'words': []
        }
        def superrost(words):
            return ''.join(filter(lambda x: ord(x) in range(ord('а'), ord('я') + 1) or
                                  ord(x) in range(ord('А'), ord('Я') + 1) or
                                  x == ' ', list(words.replace('\\n', ' '))))

        tokenizer = TweetTokenizer()
        analyzer = MorphAnalyzer()

        def preprocess(text):
            w = text.lower().split()

            filtered_words = [
                word for word in w if word not in stopwords.words('russian')]

            words = tokenizer.tokenize(' '.join(filtered_words))

            for i in range(len(words)):
                k = analyzer.parse(words[i])[0].normal_form
                word_dict[k] = words[i]
                words[i] = k
            return ' '.join(words)


        poem = text
        poem = preprocess(superrost(poem)).split()


        for w in poem:
            if w in self.olds:

                dialects['words'].append(word_dict[w])
        dialects['words'] = list(set(dialects['words']))
        return json.dumps(dialects)
