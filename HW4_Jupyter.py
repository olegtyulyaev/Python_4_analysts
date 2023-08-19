#!/usr/bin/env python
# coding: utf-8

# # Урок 4. Визуальный анализ данных

# ### Задача 1
# Постройте график
# Назовите график
# Сделайте именование оси x и оси y
# Сделайте выводы
# 
# 1. Скачать следующие данные: kc-house-data и laptop_price
# 2. Изучите стоимости недвижимости
# 3. Изучите распределение квадратуры жилой
# 4. Изучите распределение года постройки

# In[27]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[45]:


df = pd.read_csv('kc_house_data.csv', encoding = 'latin-1')
df.head(10)


# In[29]:


plt.figure(figsize=(10, 4))
sns.histplot(df['price'])
plt.ticklabel_format(style='plain')
plt.title('Распределение стоимости недвижимости')
plt.xlabel('Стоимость')
plt.ylabel('Количество');


# In[30]:


plt.figure(figsize=(10, 4))
sns.histplot(df['sqft_living'])
plt.ticklabel_format(style='plain')
plt.title('Распределение жилой площади')
plt.xlabel('Площадь')
plt.ylabel('Количество');


# In[31]:


sns.histplot(df['yr_built'], bins=30)

plt.title('Год постройки')
plt.xlabel('Год')
plt.ylabel('Количество')
plt.grid();


# #### Выводы
# 
# - Распределение стоимости недвижимости, показало, что большинство домов стоят порядка 900к;
# - Больше всего домов от 1500 до 2500 кв.м;
# - Распределение года постройки, показало, что стабильное количество было на уровне - 1950-2000 г, но после резкого скачка 2000-2009 г, количество сново стала на уровне - 1950-2000 г.

# ### Задача 2
# 
# 1. Изучите распределение домов от наличия вида на набережную
# - Постройте график
# - Сделайте выводы
# 
# 2. Изучите распределение этажей домов
# 3. Изучите распределение состояния домов

# In[32]:


data1 = df['waterfront'].value_counts()
data1


# In[33]:


labels = ['Есть вид', 'Нет вида']
plt.pie(data1, autopct='%1.1f%%', labels=labels)
plt.title('Распределение домов от наличия вида на набережную');


# Вывод: домов без вида на набережную менее 1%

# In[34]:


data2 = df['floors'].value_counts()
data2


# In[35]:


plt.figure(figsize=(6, 4))
sns.barplot(x = data2.index, y = data2)
plt.title('Распределение этажей домов')
plt.xlabel('Количество этажей')
plt.ylabel('Количество')
plt.xticks(rotation=30);


# In[36]:


data3 = df['condition'].value_counts()
data3


# In[37]:


plt.figure(figsize=(6, 4))
sns.barplot(x = data3.index, y = data3)
plt.title('Распределение состояния домов')
plt.xlabel('Состояние дома')
plt.ylabel('Количество');


# ### 3 задача
# Исследуйте, какие характеристики недвижимости влияют на стоимость недвижимости, с применением не менее 5 диаграмм из урока.
# Анализ сделайте в формате storytelling: дополнить каждый график письменными выводами и наблюдениями.
# 

# In[38]:


sns.jointplot(x=df['price'], y=df['sqft_living'], kind='reg');


# Вывод: размер жилой площади прямо влияет на его цену

# In[39]:


corr_matrix = df.corr(numeric_only=True)
corr_matrix = np.round(corr_matrix, 1)
corr_matrix[np.abs(corr_matrix) < 0.3] = 0
corr_matrix


# In[40]:


plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, linewidths=.5, cmap='coolwarm')
plt.title('Корреляция');


# In[46]:


sns.boxplot(x=df['price'], y=df['view'].astype('str'), whis=1.5);
plt.xlabel('Стоимость')
plt.ylabel('Вид')
plt.title('Влияние вида недвижимости на стоимость');


# Вывод: Дома с видом самаятвысокая цена у домов с оценкой 4

# In[43]:


sns.boxplot(x=df['price'], y=df['grade'].astype('str'), whis=1.5);
plt.xlabel('Стоимость')
plt.ylabel('Оценка недвижемости')
plt.title('Влияние оценки недвижимости на стоимость');


# In[48]:


sns.boxplot(x=df['price'], y=df['floors'].astype('str'), whis=2);
plt.xlabel('Стоимость')
plt.ylabel('Этажность')
plt.title('Влияние количества этажей на стоимость');


# Вывод: 2-х этажные дома самые дорогие и имеют самый баольшой вынос по ценам

# In[ ]:




