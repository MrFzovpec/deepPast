from bs4 import BeautifulSoup as bs
import requests

class Parser:
    def __init__(self):
        self.url = 'https://gufo.me/dict/ozhegov/'
        self.headers = {'accept': '*/*',
                   'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}


    def find(self, content):
        session = requests.Session()
        request = session.get(self.url + str(content), headers=self.headers)
        soup = bs(request.text, 'html.parser')

        response = soup.article.text
        print(response)


        if response != None:
            return response
        else:
            return "Информация не найденна("
