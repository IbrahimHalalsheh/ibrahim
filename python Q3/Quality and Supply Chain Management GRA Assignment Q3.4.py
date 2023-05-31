#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[9]:


data = pd.read_csv('question_3.csv')


# In[12]:


correlation_matrix = data.corr()


# In[13]:


# positive_correlation = correlation_matrix.unstack().sort_values(ascending = False)


# In[14]:


# top_positive_pairs = positive_correlation[positive_correlation < 1].head(5)


# In[15]:


# negative_correlation = correlation_matrix.unstack().sort_values(ascending = True)


# In[16]:


# top_negative_pairs = negative_correlation[negative_correlation > -1].head(5)


# In[22]:


# print ("top 5 variables with positive correlation:")
# for pair, correlation in top_positive_pairs.items():
#     print(pair, correlation)


# In[21]:


# print("top 5 variables with negative correlation:")
# for pair, correaltion in top_negative_pairs:
#     print(pair, correlation)


# In[23]:


correlation_stacked = correlation_matrix.stack().reset_index()


# In[26]:


correlation_stacked.columns = ['Variable1', 'Variable2', 'Correlation']


# In[29]:


sorted_correlations = correlation_stacked.sort_values(by = 'Correlation', ascending = False)


# In[30]:


top_positive_pairs = sorted_correlations[sorted_correlations['Correlation'] < 1].head(5)


# In[32]:


top_negative_pairs = sorted_correlations[sorted_correlations['Correlation'] > -1].tail(5)


# In[33]:


print('Top 5 variable pairs with positive correlation:')
print(top_positive_pairs)


# In[34]:


print('Top 5 variable pairs with negative correlation:')
print(top_negative_pairs)


# In[ ]:





# In[ ]:





# In[ ]:




