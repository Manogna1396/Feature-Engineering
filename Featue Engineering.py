#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
data=pd.read_csv('C:\\Users\\chanakya balemarthy\\Pictures\\DATASETS\\cereal.csv')
data.head(2)


# In[2]:


data.isnull().sum()


# In[3]:


data.dtypes


# In[4]:


### As the column 'mfr' and 'type' are categorical variables ,replacing the missing values with most frequent value(mode)
data['mfr'].fillna(data['mfr'].mode()[0],inplace=True)
data['type'].fillna(data['type'].mode()[0],inplace=True)


# In[5]:


data.isna().sum()


# In[6]:


#### The type of missing data is 'MISSING AT RANDOM' because data is missing for 'Fruit & Fibre Dates' & 'Muesli Raisins'
#### We must replace it with 'MEAN','MEDIAN' or should drop the entire rows
#### since the count of missing  data is very small when compared with size of the data, i am choosing to drop the rows.
data.dropna(axis=0,inplace=True)


# In[7]:


data.isna().sum()


# In[ ]:




