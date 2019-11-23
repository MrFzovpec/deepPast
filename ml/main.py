from bs4 import BeautifulSoup
import requests
from datetime import date, timedelta
import re
from collections import Counter
from pymorphy2 import MorphAnalyzer




def downloadData(url):
    """Эта штука скачивает датасет из ссылки

    param url: string
    """

    tuttoarr2 = []
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)
    inputTag = soup.findAll("dl")

    for link in inputTag:
        try:
            title = link.findChildren("a",recursive=True)
            for titlea in title:
                if titlea.has_attr('href') and not titlea.has_attr('class'):
                    if 'comment' not in titlea['href']:
                        tuttoarr2.append(tuple((titlea['href'],titlea.text)))
        except IndexError:
            print('Rien')


    newarr=[]
    i =0
    for elem in tuttoarr2:
        r  = requests.get(url+elem[0]   )
        data = r.text
        soup2 = BeautifulSoup(data)
        inputTag2 = soup2.findAll("div", {"align":"justify"})
        for link in inputTag2:
            if i>5:
                break
            i+=1
            try:
                title = link.findChildren("dd",recursive=True)
                for titlea in title:
                    newarr.append(tuple((elem[1],titlea.text)))

            except IndexError:
                print('Rien')

    return newarr



def supercostul(string, iters=2):
    string = re.sub("^\s+|\n|\r|\s+$", '', string)
    string = string.lower()


    def listtostr (word):
        str =''
        for l in word:
            str += l
        return str

    def stringToList(string, punct= ['.',',',':',';','!','?','(',')', '-', '--', '"', '{', '}', '*']):
                wordList = string.split()
                i = 0
                for word in wordList:
                    word = list(word)
                    j = 0
                    for l in word:
                        if l in punct:
                            word.pop(j)
                        j+=1

                    wordList[i]=listtostr(word)
                    i += 1

                i = 0
                for word in wordList:
                    if word=='':
                        wordList.pop(i)
                    i += 1

                return wordList

    def listtostr2 (word):
        str =''
        for l in word:
            str += l+' '
        return str


    for i in range(iters):
        string = listtostr2(stringToList(string))

    return stringToList(string)


def polnay(d1, d2):
    """Считает словари

    param d1: list of strings
    param d2: list of strings
    return dictt, d1dict, d2dict: dictionary
    """


    d1 = Counter(d1)
    d2 = Counter(d2)
    dictt = {}
    d1dict = {}
    d2dict = {}
    for word in d1:
        for wordd in d2:
            if word == wordd:
                dictt[word]=d1[word]-d2[word]
            else:
                d1dict[word]=1

    for word in d2:
        if not (word in dictt):
            d2dict[word]=1

    return dictt, d1dict, d2dict

def proc(text):
    tokenizer = TweetTokenizer()
    def preprocess(text):
        words = tokenizer.tokenize(text)
        return ' '.join(words).lower()
