#!/usr/bin/env python
# coding: utf-8

# In[114]:


# Reorder it 

import matplotlib.pyplot as plt
import seaborn as sns


correlation_matrix = data.corr()

top_positive_pairs = correlation_matrix.unstack().sort_values(ascending=False)[:5]

top_negative_pairs = correlation_matrix.unstack().sort_values()[:5]

fig, axs = plt.subplots(2, 5, figsize=(20, 10))

axs = axs.flatten()

for i, (var1, var2) in enumerate(top_positive_pairs.index):
    axs[i].scatter(data[var1], data[var2])
    axs[i].set_xlabel(var1)
    axs[i].set_ylabel(var2)

for i, (var1, var2) in enumerate(top_negative_pairs.index):
    axs[i + 5].scatter(data[var1], data[var2])
    axs[i + 5].set_xlabel(var1)
    axs[i + 5].set_ylabel(var2)

plt.tight_layout()


# In[ ]:




