#!/usr/bin/env python
# coding: utf-8

# In[81]:


import wikipedia
wikipedia.set_lang('ru')
word = 'барбер'


# In[83]:


wikipedia.set_lang('ru')
answ = wikipedia.search(word)[0]
try:
    print('Основной запрос:')
    print(wikipedia.summary(answ))
    print('---------------------------------')
    print('---------------------------------')
    print('Возможны и другие запросы:')
    print('---------------------------------')
    for i in range(len(wikipedia.search(word))):
        answ = wikipedia.search(word)[i]
        print(wikipedia.summary(answ))
        print('---------------------------------')
except Exception:
    print('В Википедии статьи по слову '+answ+' не найдено')
    print('Возможно вы имели в виду:')
    for i in range(len(wikipedia.search(word))):
        answ = wikipedia.search(word)[i]
        print(answ)   


# In[ ]:




