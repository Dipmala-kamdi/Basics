#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# save filepath to variable for easier access
file_path = 'D:/Project/Technocolabs/IPL Ball-by-Ball 2008-2020.csv'
# read the data and store data in DataFrame titled melbourne_data
ipl_data = pd.read_csv(file_path) 
# print a summary of the data in Melbourne data
ipl_data.describe()


# In[3]:


ipl_data.columns


# In[4]:


ipl_data = ipl_data.dropna(axis=0)


# In[5]:


ipl_data


# In[6]:


y = ipl_data.over


# In[7]:


ipl_features = ['inning', 'ball', 'batsman_runs', 'extra_runs', 'total_runs','non_boundary','is_wicket']


# In[8]:


X = ipl_data[ipl_features]


# In[9]:


X.describe()


# In[10]:


X.head()


# In[11]:


from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
ipl_model = DecisionTreeRegressor(random_state=1)

# Fit model
ipl_model.fit(X, y)


# In[13]:


print("The predictions are")
print(ipl_model.predict(X.head()))


# In[15]:


from sklearn.metrics import mean_absolute_error

predicted_over = ipl_model.predict(X)
mean_absolute_error(y, predicted_over)


# In[16]:


from sklearn.model_selection import train_test_split

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
# Define model
ipl_model = DecisionTreeRegressor()
# Fit model
ipl_model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = ipl_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))


# In[ ]:





# In[ ]:




