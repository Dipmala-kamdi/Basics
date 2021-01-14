#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime


# In[2]:


pd.set_option('display.max_columns', None)
data_train = pd.read_csv('C:/Users/Adika/Downloads/aug_train.csv')
data_test = pd.read_csv('C:/Users/Adika/Downloads/aug_test.csv')


# In[3]:


d_train = data_train.target  
# Concatenate training and test sets 
data = pd.concat([data_train.drop(['target'], axis=1), data_test])


# In[4]:


data.columns


# In[5]:


data.head()


# In[6]:


data.info()


# In[7]:


data.describe()


# In[8]:


data = data.drop_duplicates()


# In[9]:


import seaborn as sns


# In[10]:


sns.countplot(x='city_development_index', data=data)
plt.xticks(rotation=90)


# In[11]:


data['city_development_index'] = np.where(data['enrolled_university']=='Full time course', 'no_enrollment', data['city_development_index'])

data['city_development_index'] = np.where(data['education_level']=='Graduate','Masters', data['city_development_index'])

data['city_development_index'] = np.where(data['major_discipline']=='Business Degree','Other', data['city_development_index'])


# In[12]:



data['city_development_index']


# In[13]:


sns.countplot(x='city_development_index', data=data)
plt.xticks(rotation=90)


# In[14]:


data['major_discipline'].unique()


# In[15]:


data['major_discipline'] = np.where(data['major_discipline']=='Humanities','Other', data['major_discipline'])


# In[16]:


data['major_discipline']


# In[ ]:




