#!/usr/bin/env python
# coding: utf-8

# In[52]:


#Q1.1


# In[68]:


import pandas as pd


# In[69]:


import matplotlib.pyplot as plt


# In[71]:


Measurements = pd.read_excel('question_1_2.xlsx', header = 0, sheet_name = 'Measurements')


# In[72]:


print(Measurements)


# In[73]:


result = Measurements.groupby('Product Code').agg({'T_Height':['mean','std'], 'T_Weight':['mean','std']})


# In[74]:


print(result)

