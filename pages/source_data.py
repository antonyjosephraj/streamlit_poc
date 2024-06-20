import streamlit as st
import pandas as pd

st.title('SOURCE DATA')      

st.subheader('Investments:')      
investments=pd.read_csv('./inputs/investments.csv') 
st.write(investments.head())

st.subheader('Investments Details:')     
investments_details=pd.read_csv('./inputs/investments_details.csv')    
st.write(investments_details.head())

st.subheader('Assumptions:')     
assumptions=pd.read_csv('./inputs/assumptions.csv')    
st.write(assumptions)