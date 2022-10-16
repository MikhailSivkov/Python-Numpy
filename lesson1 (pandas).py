#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Задание 1
#Импортируйте библиотеку Pandas и дайте ей псевдоним pd. Создайте датафрейм authors со столбцами author_id и author_name, 
#в которых соответственно содержатся данные: [1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].
#Затем создайте датафрейм book cо столбцами author_id, book_title и price, в которых соответственно содержатся данные:  
#[1, 1, 1, 2, 2, 3, 3],
#['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
#[450, 300, 350, 500, 450, 370, 290].


# In[2]:


import pandas as pd


# In[7]:


data1 ={'author_id':[1, 2, 3], 'author_name':['Тургенев', 'Чехов', 'Островский']}
authors = pd.DataFrame(data1)


# In[10]:


data2 ={'author_id':[1, 1, 1, 2, 2, 3, 3], 'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'], 'price':[450, 300, 350, 500, 450, 370, 290]}
author_name = pd.DataFrame(data2)


# In[ ]:


#Задание 2
#Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.


# In[12]:


authors_price = pd.merge(authors, author_name, on='author_id', how='inner')


# In[ ]:


#Задание 3
#Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.


# In[14]:


top5=authors_price.nlargest(5, 'price')


# In[ ]:


#Задание 4
#Создайте датафрейм authors_stat на основе информации из authors_price. В датафрейме authors_stat должны быть четыре столбца:
#author_name, min_price, max_price и mean_price,
#в которых должны содержаться соответственно имя автора, минимальная, максимальная и средняя цена на книги этого автора.


# In[35]:


#data3=
authors_stat=pd.DataFrame(data1)

authors_price['author_name'].unique()
authors_stat['max_price']=authors_price['price'].max()
authors_stat['min_price']=authors_price['price'].min()
authors_stat['mean_price']=authors_price['price'].mean()
authors_stat


# In[23]:


authors_price.groupby('author_name')['price'].max


# In[59]:


max_p=authors_price.groupby('author_name').agg({'price':max}) 
min_p=authors_price.groupby('author_name').agg({'price':min})
mean_p=authors_price.groupby('author_name').agg({'price':['mean']})


# In[60]:


min_max = pd.merge(max_p, min_p, on='author_name')
authors_stat=pd.merge(min_max, mean_p, on='author_name')
authors_stat


# In[61]:


authors_stat=authors_stat.rename(columns={'price_x':'max_price', 'price_y':'min_price', '(price, mean)':'mean_price'})
authors_stat


# In[ ]:




