#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Exclude id


# In[17]:


import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv('question_3.csv')


# In[9]:


numeric_columns = df.select_dtypes(include = 'number').columns


# In[13]:


corr_matrix = df[numeric_columns].corr()


# In[14]:


corr_matrix


# In[20]:


plt.figure(figsize = (10,8))
sns.heatmap(corr_matrix, annot = True, cmap = 'coolwarm', square = True)
plt.title('Correlation Matrix')
plt.show()


# In[ ]:




