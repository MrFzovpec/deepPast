#!/usr/bin/env python
# coding: utf-8

# In[59]:


import wikipedia
wikipedia.set_lang('ru')


# In[60]:


wikipedia.set_lang('ru')
answ = wikipedia.search(word)[0]
try:
    return wikipedia.summary(answ)
except Exception:
    return 'В Википедии статьи по слову '+answ+' не найдено'


# In[67]:





# In[ ]:




