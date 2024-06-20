import streamlit as st
import numpy as np
import pandas as pd


# Investments
st.subheader(':blue[Investments:]')
investments = pd.read_csv('./inputs/investments.csv')
investments_edited_df = st.data_editor(investments)

# Investments Details
st.subheader(':blue[Investments Details:]')      
investments_details = pd.read_csv('./inputs/investments_details.csv') 
investments_details_edited_df = st.data_editor(investments_details)
# investments_details_edited_df = st.data_editor(investments_details, num_rows="dynamic")

# Calculations
investments_edited_df['Date of Investment'] = pd.to_datetime(investments_edited_df['Date of Investment'], format='%d-%m-%Y').dt.strftime('%Y-%m-%d')
min_date = investments_edited_df['Date of Investment'].min()
investments_at_entry = investments_edited_df['Investment at entry'].sum()

# print('investments_edited_df \n', investments_edited_df['Date of Investment'])
# print('min_date \n', min_date)


investments_details_edited_df['Exit Date'] = pd.to_datetime(investments_details_edited_df['Exit Date'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')
max_date = investments_details_edited_df['Exit Date'].max()
# print('investments_details_edited_df \n', investments_details_edited_df['Exit Date'])
# print('max_date \n', max_date)

# Assumptions
st.subheader(':blue[Casual Assumptions:]')      
# columns = ["Date" ,"Low Case" ,"Base Case" ,"High Case" ,"Comments"]
# assumptions = pd.DataFrame(columns=columns)
# st.write(assumptions)

date_range = pd.date_range(start=min_date, end=max_date, freq='M')
assumptions = pd.DataFrame(date_range, columns=['Date'])
assumptions['Date'] = pd.to_datetime(assumptions['Date'], format='%Y-%m-%d').dt.strftime('%Y-%m-%d')
assumptions[["Low Case" ,"Base Case" ,"High Case" ,"Comments"]] = None
assumptions.loc[0, ["Low Case" ,"Base Case" ,"High Case"]] = [-investments_at_entry ,-investments_at_entry ,-investments_at_entry]
# st.write(assumptions)
assumptions_edited_df = st.data_editor(assumptions)

st.subheader(':blue[Valuation Waterfall Output:]')


column_values_list = investments_details_edited_df['Scenario'].tolist()
column_values_values = investments_details_edited_df['EBITDA at Exit'].tolist()
column_values_values2 = investments_details_edited_df['Multiple at Exit'].tolist()


# st.write(column_values_list)

data2 = {
    'Calc': ['ARR /Rev /EBITDA', 'Multiple'],
    'Entry': [200,10]
}
data_v2 = pd.DataFrame(data2)
# data_v2 = pd.DataFrame(columns=column_values_list)
data_v2[column_values_list] = None
data_v2.loc[0, column_values_list] = [column_values_values]
data_v2.loc[1, column_values_list] = [column_values_values2]

# st.write(data_v2)

data3 = {
    'Calc': ['Net Debt', 'Cash flow adj'],
    'Entry': [None,None]
}
data_v3 = pd.DataFrame(data3)
data_v3[column_values_list] = None
# data_v3_edited_df = st.data_editor(data_v3, hide_index=-1)

# data4 = {
#     'Calc': ['Equity'],
#     'Entry': [None]
# }
# data_v4 = pd.DataFrame(data4)
# st.write(data_v2)



# with st.container(height=300, border=True, backgroundColor='red'):
with st.container(height=300, border=True):
    st.write(data_v2)

    data_v3_edited_df = st.data_editor(data_v3, hide_index=-1)



