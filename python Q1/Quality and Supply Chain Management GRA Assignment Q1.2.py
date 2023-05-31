#!/usr/bin/env python
# coding: utf-8

# In[74]:


#Q1.2


# In[75]:


import pandas as pd


# In[76]:


import matplotlib.pyplot as plt


# In[77]:


df_measurements = pd.read_excel('question_1_2.xlsx', header = 0, sheet_name = 'Measurements')
df_production = pd.read_excel('question_1_2.xlsx', header = 0, sheet_name = 'Production_Sequence')
df_specifications = pd.read_excel('question_1_2.xlsx', header = 0, sheet_name = 'Specifications')


# In[78]:


print(df_measurements)
print(df_production)
print(df_specifications)


# In[79]:


# sorted_data = measurement.sort_values(by = ['Product Code', 'T_Height'], ascending = [True,False])


# In[80]:


df_merged = df_measurements.merge(df_production[['Variant', 'Product_Family']], left_on = 'Product_Code', right_on = 'Variant')


# In[81]:


df_merged = df_merged.merge(df_specifications[['Product_Code', 'T_Name', 'USL']], left_on =  'Product_Code', right_on = 'Product_Code')


# In[82]:


df_defective = df_merged[df_merged['T_Height'] > df_merged['USL']]


# In[83]:


defective_counts = df_defective['Product_Family'].value_counts()


# In[84]:


cumulative_percentage = defective_counts.cumsum() / defective_counts.sum()


# In[85]:


fig, ax1 = plt.subplots()


# In[86]:


ax1.bar(defective_counts.index, defective_counts.values, color = 'tab:red')
ax1.set_ylabel('Defective Units', color = 'tab:red')
ax1.tick_params('y', color = 'tab:red')


# In[87]:


ax2 = ax1.twinx()
ax2.plot(defective_counts.index, cumulative_percentage.values, marker = 'o', color = 'tab:blue')
ax2.axhline(0.8, color = 'tab:green', linestyle = '--')
ax2.set_ylabel('Cumulative Percentage', color = 'tab:blue')
ax2.tick_params('y', color = 'tab:blue')


# In[88]:


plt.title('Pareto Chart - Defective Units by Product Family')
plt.xlabel('Product Family')


# In[89]:


plt.show()


# In[91]:


# print(sorted_data)


# In[ ]:


# specifications =  pd.read_excel('question_1_2.xlsx', header = 1, sheet_name = 'Specifications')


# In[ ]:


# specifications


# In[ ]:


# defective_parts_count = measurements


# In[ ]:


# defective_parts_count = measurements[measurements['T_Height'] > specifications.loc[specifications['T_Name'] == 'T_height', 'USL'].iloc[0]]['Product Code'].value_counts()


# In[ ]:


# sorted_defective_parts_count = defective_parts_count.sort_values(ascending = False)


# In[ ]:


# cumulative_percentage = sorted_defective_parts_count.cumsum() / sorted_defective_parts_count.sum()*100


# In[ ]:


# fig, ax1 = plt.subplots()


# In[ ]:


# ax1.bar(sorted_defective_parts_count.index, sorted_defective_parts_count.values, color = 'tab:blue')


# In[61]:


# ax1.set_xlabel('Product Family')


# In[62]:


# ax1.set_ylabel('Defective parts Count', color = 'tab:blue')


# In[63]:


# ax1.tick_params('y', color = 'tab:blue')


# In[64]:


# ax2 = ax1.twinx()


# In[94]:


# ax2.plot(sorted_defective_parts_count.index, cumulative_percentage, color = 'tab:red', marker = 'o')


# In[95]:


# ax2.set_ylabel('Cumulative Percentage', color = 'tab:red')


# In[96]:


# ax2.tick_params('y', colors = 'tab:red')


# In[97]:


# ax1.set_title('Pareto Chart - Defective Parts by Product Family')


# In[98]:


# ax1.set_xticks(range(len(sorted_defective_parts_count)))


# In[99]:


# ax1.set_xticklabels(sorted_defective_parts_count.index, rotation=90)
# 


# In[100]:


# plt.show()


# In[101]:


# import pandas as pd
# import matplotlib.pyplot as plt

# # Load the data from Excel
# measurements_df = pd.read_excel('question_1_2.xlsx', sheet_name='Measurements')
# specifications_df = pd.read_excel('question_1_2.xlsx', sheet_name='Specifications')

# # Merge the measurements and specifications dataframes on 'Product Code'
# merged_df = measurements_df.merge(specifications_df, on='Product Code')

# # Filter the merged dataframe for measurements greater than the upper limit
# defective_parts = merged_df[merged_df['T_Height'] > merged_df['USL']]

# # Count the number of defective parts by product code
# defective_parts_count = defective_parts['Product Code'].value_counts()

# # Sort the product families in descending order of defective parts count
# sorted_defective_parts_count = defective_parts_count.sort_values(ascending=False)

# # Calculate the cumulative percentage
# cumulative_percentage = sorted_defective_parts_count.cumsum() / sorted_defective_parts_count.sum() * 100

# # Create the Pareto chart
# fig, ax1 = plt.subplots()

# # Bar plot for defective parts count
# ax1.bar(sorted_defective_parts_count.index, sorted_defective_parts_count.values, color='tab:blue')
# ax1.set_xlabel('Product Code')
# ax1.set_ylabel('Defective Parts Count', color='tab:blue')
# ax1.tick_params('y', colors='tab:blue')

# ax2 = ax1.twinx()

# # Line plot for cumulative percentage
# ax2.plot(sorted_defective_parts_count.index, cumulative_percentage, color='tab:red', marker='o')
# ax2.set_ylabel('Cumulative Percentage', color='tab:red')
# ax2.tick_params('y', colors='tab:red')

# # Set chart title and axis labels
# ax1.set_title('Pareto Chart - Defective Parts by Product Code (T_Height)')
# ax1.set_xticklabels(sorted_defective_parts_count.index, rotation=90)

# plt.show()


# In[ ]:




