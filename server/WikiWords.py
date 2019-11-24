#!/usr/bin/env python
# coding: utf-8

# In[115]:


import requests 
from bs4 import BeautifulSoup
answer = requests.get('https://ru.wiktionary.org/wiki/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0')  
soup = BeautifulSoup(answer.text, 'html.parser')
print(soup.find('ol').find('li').text)

