#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Path of the file to read
tweets_filepath = "D:/Project/Technocolabs/mydata.csv"


# In[3]:


# Read the file into a variable fifa_data
tweets_data = pd.read_csv(tweets_filepath, index_col="date", parse_dates=True)


# In[4]:


# Print the first 5 rows of the data
tweets_data.head()


# In[6]:


tweets_data.source


# In[7]:


tweets_data.source == "Twitter for iphone"


# In[8]:


tweets_data.retweets == 0


# In[9]:


tweets_data.retweets.describe()


# In[10]:


tweets_data.groupby('retweets').retweets.count()


# In[11]:


tweets_data.groupby('retweets').retweets.max()


# In[12]:


tweets_data.dtypes


# In[13]:


tweets_data[pd.isnull(tweets_data)]


# In[14]:


tweets_data.fillna("Unknown")


# In[ ]:




