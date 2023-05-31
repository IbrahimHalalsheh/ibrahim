#!/usr/bin/env python
# coding: utf-8

# In[50]:


import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('question_3.csv')

# Exclude non-numeric and unsuitable columns
excluded_columns = ['ID', 'quality']
columns = [col for col in df.columns if col not in excluded_columns and pd.api.types.is_numeric_dtype(df[col])]

# Define the layout for the matrix of charts
num_rows = 3
num_cols = 4
fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 10))

# Generate histograms for each data column
for i in range(len(columns)):
    row = i // num_cols
    col = i % num_cols
    ax = axes[row, col]
    ax.hist(df.iloc[:, i], bins=10)
    ax.set_title(columns[i])
    ax.set_xlabel('Values')
    ax.set_ylabel('Frequency')

# Adjust spacing between subplots
plt.tight_layout()

# Display the matrix of charts
plt.show()

