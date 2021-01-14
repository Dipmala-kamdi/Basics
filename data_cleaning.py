#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


import numpy as np


# In[5]:


mydata = pd.read_csv("D:/Project/Technocolabs/Data Cleaning/archive/vaccination_tweets.csv")


# In[6]:


# set seed for reproducibility
np.random.seed(0)


# In[7]:


mydata.head()


# In[8]:


# get the number of missing data points per column
missing_values_count = mydata.isnull().sum()


# In[9]:


# look at the # of missing points in the first ten columns
missing_values_count[0:10]


# In[10]:


missing_values_count


# In[11]:


# how many total missing values do we have?
total_cells = np.product(mydata.shape)
total_missing = missing_values_count.sum()

# percent of data that is missing
percent_missing = (total_missing/total_cells) * 100
print(percent_missing)


# In[12]:


# remove all the rows that contain a missing value
mydata.dropna()


# In[14]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




