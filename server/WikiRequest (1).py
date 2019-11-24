#!/usr/bin/env python
# coding: utf-8

# In[75]:


import wikipedia
wikipedia.set_lang('ru')


# In[80]:


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


# In[ ]:




