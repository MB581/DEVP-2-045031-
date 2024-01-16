#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the data
data = pd.read_excel('red wine.xlsx')

# Set the page title (call this only once)
st.set_page_config(page_title='Red Wine Dashboard', layout='wide')

# Title for the dashboard
st.title('Red Wine Quality Dashboard')

# Slicer for filtering data by quality
selected_quality = st.selectbox('Select Wine Quality:', sorted(data['quality'].unique()))

# Filter data based on selected quality
filtered_data = data[data['quality'] == selected_quality]

# Display filtered data
st.write(f'## Filtered Data for Quality {selected_quality}')
st.dataframe(filtered_data)

# Dataset Preview
st.write('## Dataset Preview')
st.dataframe(data.head())

# Summary statistics
st.write('## Summary Statistics')
st.write(data.describe())

# Slicer for the correlation heatmap
selected_feature_corr = st.selectbox('Select Feature for Correlation Heatmap:', data.columns)
corr_selected_feature = data[[selected_feature_corr, 'quality']].corr()

# Correlation heatmap
st.write(f'## Correlation Heatmap for {selected_feature_corr} vs. Quality')
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr_selected_feature, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, ax=ax)
st.pyplot(fig)

# Slicer for the wine quality distribution histogram
selected_feature_hist = st.selectbox('Select Feature for Wine Quality Distribution:', data.columns)

# Histogram of wine quality
st.write(f'## Distribution of Wine Quality based on {selected_feature_hist}')
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(data[selected_feature_hist], bins=6, kde=True, color='skyblue', ax=ax)
st.pyplot(fig)

# Slicer for the scatter plot of alcohol content vs. quality
selected_feature_scatter_x = st.selectbox('Select Feature for X-axis in Scatter Plot:', data.columns)
selected_feature_scatter_y = st.selectbox('Select Feature for Y-axis in Scatter Plot:', data.columns)

# Scatter plot of selected features
st.write(f'## Scatter Plot: {selected_feature_scatter_x} vs. {selected_feature_scatter_y}')
fig, ax = plt.subplots(figsize=(10, 8))
sns.scatterplot(x=selected_feature_scatter_x, y=selected_feature_scatter_y, data=data, hue='quality', palette='viridis', ax=ax)
st.pyplot(fig)


# In[ ]:




