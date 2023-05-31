#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[4]:


df_measurements = pd.read_excel('question_1_2.xlsx', sheet_name = 'Measurements')
df_specifications = pd.read_excel('question_1_2.xlsx', sheet_name = 'Specifications')


# In[8]:


df_filtered = df_measurements[(df_measurements['Product_Code'] == 'LIF002_Y') | (df_measurements['Product_Code'] == 'LIF001_Y')]


# In[14]:


df_merged = df_filtered.merge(df_specifications[['Product_Code', 'T_Name', 'Target']], on = 'Product_Code')


# In[19]:


df_merged['Deviation_Height'] = df_merged['T_Height'] - df_merged['Target']


# In[22]:


df_merged['Deviation_Weight'] = df_merged['T_Weight'] - df_merged['Target']


# In[26]:


avg_deviation = df_merged.groupby('Product_Code')[['Deviation_Height', 'Deviation_Weight']].mean()


# In[35]:


avg_deviation['Deviation_Height']
avg_deviation['Deviation_Weight']


# In[31]:


plt.bar(avg_deviation.index, avg_deviation['Deviation_Height'], label = 'T_Height', color = 'tab:red')
plt.bar(avg_deviation.index, avg_deviation['Deviation_Weight'], label = 'T_Weight', color = 'tab:blue')
plt.axhline(0, color = 'black', linestyle = '--')
plt.xlabel('Product Family')
plt.ylabel('Average Deviation from Target')
plt.title('Comparison of Process Control for Variant Y')
plt.legend()
plt.show()


# In[ ]:




