#!/usr/bin/env python
# coding: utf-8

# In[173]:


import pandas as pd 
import matplotlib.pyplot as plt


# In[174]:


df_measurements = pd.read_excel('question_1_2.xlsx', sheet_name = 'Measurements')


# In[175]:


plt.figure(figsize = (10,6))


# In[176]:


for lot in df_measurements['Lot_No'].unique():
    df_lot = df_measurements[df_measurements['Lot_No'] == lot]
    plt.plot(df_lot.index, df_lot['T_Height'], marker = 'o', label = lot)
    plt.xlabel('Index')
    plt.ylabel('Height Measurements')
    plt.title('Height Measurements Variation by Lot')
    plt.legend()
    plt.show()


# In[177]:


plt.figure(figsize = (10,6))


# In[182]:


for lot in df_measurements['Lot_No'].unique():
    df_lot = df_measurements[df_measurements['Lot_No'] == lot]
    plt.plot(df_lot.index, df_lot['T_Weight'], marker = 'o', label = lot)
    plt.xlabel('Index')
    plt.ylabel('Weight Measurements')
    plt.title('Weight Measurements Variation by Lot')
    plt.legend()
    plt.show()


# In[ ]:




