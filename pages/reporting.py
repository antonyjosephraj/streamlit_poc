import streamlit as st
import numpy as np
import pandas as pd
import numpy_financial as npf
from streamlit import session_state as ss, data_editor as de, rerun as rr
from st_aggrid import AgGrid, GridOptionsBuilder
import plotly.graph_objects as go


def main(): 

    # Investments Details
    # st.subheader(':blue[Investments Details:]')      
    # investments_details = pd.read_csv('./inputs/investments_details.csv') 
    # investments_details['Exit Date'] = pd.to_datetime(investments_details['Exit Date'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')

    data_investments_details_pf1 = ss.investments_data_pf1
    data_investments_amount_pf1 = ss.investments_amount_pf1
    data_revenue_return_pf1 = ss.revenue_return_pf1


    data_investments_details_pf2 = ss.investments_data_pf2
    data_investments_amount_pf2 = ss.investments_amount_pf2
    data_revenue_return_pf2 = ss.revenue_return_pf2

    data_investments_details_pf3 = ss.investments_data_pf3
    data_investments_amount_pf3 = ss.investments_amount_pf3
    data_revenue_return_pf3 = ss.revenue_return_pf3

    data = {'Name': ['Portco 1', 'Portco 2', 'Portco 3']}
    df = pd.DataFrame(data)

    # Add a column with a dropdown list
    for i in df.index:
        df.at[i, 'Scenario'] = st.selectbox('Select Action:', ['Low Case', 'High Case', 'Base case'], key=i)
        if i  == 0:
            for pf1 in data_investments_details_pf1.index:
                # st.write(data_investments_details_pf1.at[pf1, 'Scenario'])
                if df.at[0, 'Scenario'] == data_investments_details_pf1.at[pf1, 'Scenario']:
                    df.at[0, 'Date of Investment'] = data_investments_amount_pf1.iloc[0]['Date of Investment']
                    df.at[0, 'Invested Amount'] = data_investments_details_pf1.at[pf1, 'Invested Amount']
                    df.at[0, 'EBITDA at Entry'] = data_investments_amount_pf1.iloc[0]['EBITDA at entry']
                    df.at[0, 'EBITDA at Exit'] = data_investments_details_pf1.at[pf1, 'EBITDA at Exit']
                    df.at[0, 'Multiple at entry'] = data_investments_amount_pf1.iloc[0]['Multiple at Entry']
                    df.at[0, 'Multiple at Exit'] = data_investments_details_pf1.at[pf1, 'Multiple at Exit']
                    df.at[0, 'Exit Date'] = data_investments_details_pf1.at[pf1, 'Exit Date']
                    df.at[0, 'Return (calculated)'] = data_revenue_return_pf1.at[0, 'Return (calculated)']
                    df.at[0, 'IRR (calculated)'] = data_revenue_return_pf1.at[0, 'IRR (calculated)']

        if i  == 1:
            for pf1 in data_investments_details_pf2.index:
                # st.write(data_investments_details_pf2.at[pf1, 'Scenario'])
                if df.at[1, 'Scenario'] == data_investments_details_pf2.at[pf1, 'Scenario']:
                    df.at[1, 'Date of Investment'] = data_investments_amount_pf2.iloc[0]['Date of Investment']
                    df.at[1, 'Invested Amount'] = data_investments_details_pf2.at[pf1, 'Invested Amount']
                    df.at[1, 'EBITDA at Entry'] = data_investments_amount_pf2.iloc[0]['EBITDA at entry']
                    df.at[1, 'EBITDA at Exit'] = data_investments_details_pf2.at[pf1, 'EBITDA at Exit']
                    df.at[1, 'Multiple at entry'] = data_investments_amount_pf2.iloc[0]['Multiple at Entry']
                    df.at[1, 'Multiple at Exit'] = data_investments_details_pf2.at[pf1, 'Multiple at Exit']
                    df.at[1, 'Exit Date'] = data_investments_details_pf2.at[pf1, 'Exit Date']
                    df.at[1, 'Return (calculated)'] = data_revenue_return_pf2.at[1, 'Return (calculated)']
                    df.at[1, 'IRR (calculated)'] = data_revenue_return_pf2.at[1, 'IRR (calculated)']

        
        if i  == 2:
            for pf1 in data_investments_details_pf3.index:
                # st.write(data_investments_details_pf3.at[pf1, 'Scenario'])
                if df.at[2, 'Scenario'] == data_investments_details_pf3.at[pf1, 'Scenario']:
                    df.at[2, 'Date of Investment'] = data_investments_amount_pf3.iloc[0]['Date of Investment']
                    df.at[2, 'Invested Amount'] = data_investments_details_pf3.at[pf1, 'Invested Amount']
                    df.at[2, 'EBITDA at Entry'] = data_investments_amount_pf3.iloc[0]['EBITDA at entry']
                    df.at[2, 'EBITDA at Exit'] = data_investments_details_pf3.at[pf1, 'EBITDA at Exit']
                    df.at[2, 'Multiple at entry'] = data_investments_amount_pf3.iloc[0]['Multiple at Entry']
                    df.at[2, 'Multiple at Exit'] = data_investments_details_pf3.at[pf1, 'Multiple at Exit']
                    df.at[2, 'Exit Date'] = data_investments_details_pf3.at[pf1, 'Exit Date']
                    df.at[2, 'Return (calculated)'] = data_revenue_return_pf3.at[2, 'Return (calculated)']
                    df.at[2, 'IRR (calculated)'] = data_revenue_return_pf3.at[2, 'IRR (calculated)']
    
    st.write(df)

    total_investment_amout = df['Invested Amount'].sum()
    total_return_amount = df['Return (calculated)'].sum()

    fun_level_data = {
        'Invested Amount': [total_investment_amout],
        'Return (calculated)': [total_return_amount]
    }
    fun_level_data_df = pd.DataFrame(fun_level_data)

    st.subheader('Total of Fund Level - Amount')
    st.write(fun_level_data_df)

    
    # df = pd.DataFrame({
    #     'Column 1': [st.selectbox('d',options), st.selectbox('d',options), st.selectbox('d',options)],
    #     'Column 2': ['A', 'B', 'C']
    # })

    # def add_dropdowns(dataframe):
    #     # Example function to add dropdowns
    #     return dataframe

    # st.dataframe(add_dropdowns(df))

    # Create a sample dataframe
    # data = {
    #     'Category': ['Fruit', 'Vegetable', 'Fruit', 'Meat', 'Vegetable'],
    #     'Subcategory': ['Apple', 'Carrot', 'Banana', 'Beef', 'Broccoli']
    # }

    # df = pd.DataFrame(data)

    # # Create the primary dropdown for Category
    # selected_category = st.selectbox("Select Category", df['Category'].unique())

    # # Filter the dataframe based on the selected category
    # filtered_df = df[df['Category'] == selected_category]

    # # Create a dictionary for dependent dropdown options
    # dependent_dropdown_options = {
    #     'options': filtered_df['Subcategory'].unique().tolist(),
    #     'default': None  # You can set a default value here if needed
    # }

    # # Display the dependent dropdown using st_aggrid
    # grid_options = GridOptionsBuilder.from_dataframe(filtered_df).build()
    # AgGrid(filtered_df, gridOptions=grid_options, data_editor=dependent_dropdown_options)


    # @st.cache_data
    def get_chart_83992296():

        fig = go.Figure(go.Waterfall(
            name = "20", orientation = "v",
            measure = ["relative", "relative", "total", "relative", "relative", "total"],
            x = ["Sales", "Consulting", "Net revenue", "Purchases", "Other expenses", "Profit before tax"],
            textposition = "outside",
            text = ["+60", "+80", "", "-40", "-20", "Total"],
            y = [60, 80, 0, -40, -20, 0],
            connector = {"line":{"color":"rgb(63, 63, 63)"}},
        ))

        fig.update_layout(
                title = "Profit and loss statement 2018",
                showlegend = True
        )

        tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
        with tab1:
            st.plotly_chart(fig, theme="streamlit")
        # with tab2:
        #     st.plotly_chart(fig, theme=None)

    get_chart_83992296()


if __name__ == '__main__':
    main()


    # fig = go.Figure(go.Waterfall(
    #         x = ["Sales", "Consulting", "Net revenue", "Purchases", "Other expenses", "Profit before tax"],
    #         y = [60, 80, 0, -40, -20, 0],
    #     ))
    #     st.plotly_chart(fig, theme="streamlit")
    