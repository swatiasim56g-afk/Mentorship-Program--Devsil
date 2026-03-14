# import libraries 
import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
# data title 
st.title('Data Analysis Application')
st.subheader('This is a simple data analysis application created by Muhammad Asim')
# create a dropdown list to choose a data set
data_set = st.selectbox(
    'Select a data set',
    ('Iris', 'Cancer', 'Diabetes'))
# create a button to load the data set  
if st.button('Load data'):
    if data_set == 'Iris':
        iris = sns.load_dataset('iris')
        st.write(iris.head())
    elif data_set == 'Cancer':
        cancer = sns.load_dataset('breast_cancer')
        st.write(cancer.head())
    elif data_set == 'Diabetes':
        diabetes = sns.load_dataset('diabetes')
        st.write(diabetes.head())

# button to upload custom dataset 
if st.button('Upload data'):
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df.head())
# display the dataset
st.write(data_set)
# Now display the number of rows and columns from the selected data
st.write('Number of rows :', data_set.shape[0])
st.write('Number of columns :', data_set.shape[1])
# display the column names of the selected data
st.write('Column names :', data_set.columns)
# now print the null values if those are > 0
if data_set.isnull().sum().sum() > 0:
    st.write('Null values :', data_set.isnull().sum())
else:
    st.write('No null values found')
# display the summary of stastistics of the selected data
st.write(data_set.describe())
# plot the data 
if plot_type == 'line':
    st.line_chart(data_set)
elif plot_type == 'bar':
    st.bar_chart(data_set)
elif plot_type == 'area':
    st.area_chart(data_set)
elif plot_type == 'histogram':
    st.histogram(data_set)
elif plot_type == 'boxplot':
    st.boxplot(data_set)
else:
    st.write('Invalid plot type')

