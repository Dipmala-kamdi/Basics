#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[16]:


# Path of the file to read
tweets_filepath = "D:/Project/Technocolabs/mydata.csv"


# In[17]:


# Read the file into a variable fifa_data
tweets_data = pd.read_csv(tweets_filepath, index_col="date", parse_dates=True)


# In[18]:


# Print the first 5 rows of the data
tweets_data.head()


# In[19]:


# Set the width and height of the figure
plt.figure(figsize=(16,6))


# In[20]:


# Line chart showing how tweets rankings evolved over time 
sns.lineplot(data=tweets_data, x= tweets_data.retweets, y=tweets_data.user_followers)


# In[21]:


tweets_data.head()


# In[24]:


sns.lineplot(data=tweets_data[['user_followers','user_friends','user_favourites','retweets','favorites']])


# In[27]:


# Set the width and height of the figure
plt.figure(figsize=(10,6))

# Add title
plt.title("tweets by user")

# Bar chart
sns.barplot(x=tweets_data.retweets, y=tweets_data['source'])


# In[28]:


# Set the width and height of the figure
plt.figure(figsize=(14,7))

# Add title
plt.title("Tweeter data")

# Heatmap showing average arrival delay for each airline by month
sns.heatmap(data=tweets_data, annot=True)


# In[30]:


# KDE plot 
sns.kdeplot(data=tweets_data['retweets'], shade=True)


# In[32]:


# 2D KDE plot
sns.jointplot(x=tweets_data['retweets'], y=tweets_data['favorites'], kind="kde")


# In[33]:


sns.scatterplot(x=tweets_data['retweets'], y=tweets_data['favorites'], hue=tweets_data['user_verified'])


# In[ ]:




