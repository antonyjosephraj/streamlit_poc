import streamlit as st
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

st.title('POC')      
st.text('Identify the specifics of data input and delineate the operational functionalities.')

st.image('ai.jpg')


st.title("CHART'S")      
data=pd.read_csv('data_inputs.csv')    
df= pd.DataFrame(   data,    columns=['Invested Amount', 'Multiple at Exit'])
st.line_chart(df)

st.markdown('Dataset :')   
data=pd.read_csv('sample_data.csv')    
st.write(data.head())