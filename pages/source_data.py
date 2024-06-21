import streamlit as st
import numpy as np
import pandas as pd
import numpy_financial as npf
from streamlit import session_state as ss, data_editor as de, rerun as rr


def main():

    # Investments
    st.subheader(':blue[Investments:]')
    investments = pd.read_csv('./inputs/investments.csv')
    investments_edited_df = st.data_editor(investments)

    # Investments Details
    st.subheader(':blue[Investments Details:]')      
    investments_details = pd.read_csv('./inputs/investments_details.csv') 
    investments_details['Exit Date'] = pd.to_datetime(investments_details['Exit Date'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')
    if 'investments_data' not in ss:
        ss.investments_data = pd.DataFrame(investments_details)

    investments_details_v2 = de(ss.investments_data)

    # investments_details.loc[investments_details['Scenario'] == 'Low Case', 'Invested Amount'] = 30000
    # investments_details_edited_df = st.data_editor(investments_details)
    # print('ppppppppppppppppp', investments_details_edited_df)
    # investments_details_edited_df = st.data_editor(investments_details, num_rows="dynamic")

    # Calculations
    investments_edited_df['Date of Investment'] = pd.to_datetime(investments_edited_df['Date of Investment'], format='%d-%m-%Y').dt.strftime('%Y-%m-%d')
    min_date = investments_edited_df['Date of Investment'].min()
    investments_at_entry = investments_edited_df['Investment at entry'].sum()

    # print('investments_edited_df \n', investments_edited_df['Date of Investment'])
    # print('min_date \n', min_date)


    # investments_details_v2['Exit Date'] = pd.to_datetime(investments_details_v2['Exit Date'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')
    max_date = investments_details_v2['Exit Date'].max()
    # print('investments_details_edited_df \n', investments_details_edited_df['Exit Date'])
    # print('max_date \n', max_date)

    print('max_date', max_date)

    # Assumptions
    st.subheader(':blue[Casual Assumptions:]')      
    # columns = ["Date" ,"Low Case" ,"Base Case" ,"High Case" ,"Comments"]
    # assumptions = pd.DataFrame(columns=columns)
    # st.write(assumptions)

    date_range = pd.date_range(start=min_date, end=max_date, freq='M')
    assumptions = pd.DataFrame(date_range, columns=['Date'])
    assumptions['Date'] = pd.to_datetime(assumptions['Date'], format='%Y-%m-%d').dt.strftime('%Y-%m-%d')
    assumptions[["Low Case" ,"Base Case" ,"High Case" ,"Comments"]] = None
    assumptions.loc[0, ["Low Case" ,"Base Case" ,"High Case"]] = [ -investments_at_entry ,-investments_at_entry ,-investments_at_entry]
    # st.write(assumptions)

    if 'assumptions_data' not in ss:
        ss.assumptions_data = pd.DataFrame(assumptions)

    assumptions_edited_df_v2 = de(ss.assumptions_data)

    st.write(ss)

    # assumptions_edited_df = st.data_editor(assumptions)

    investment_update = assumptions_edited_df_v2

    low_case_sum_of_negatives = investment_update[investment_update['Low Case'] < 0]['Low Case'].sum()
    base_case_sum_of_negatives = investment_update[investment_update['Base Case'] < 0]['Base Case'].sum()
    high_case_sum_of_negatives = investment_update[investment_update['High Case'] < 0]['High Case'].sum()


    if not ss.assumptions_data.equals(assumptions_edited_df_v2):
        print('22222222222')
        ss.assumptions_data = assumptions_edited_df_v2
        # ss.investments_data.loc[ss.investments_data['Invested Amount'].notna(), 'Multiple at Exit'] = ss.investments_data['Invested Amount']
        ss.investments_data.loc[ss.investments_data['Scenario'] == 'Low Case', 'Invested Amount'] = abs(low_case_sum_of_negatives)
        ss.investments_data.loc[ss.investments_data['Scenario'] == 'Base case', 'Invested Amount'] = abs(base_case_sum_of_negatives)
        ss.investments_data.loc[ss.investments_data['Scenario'] == 'High Case', 'Invested Amount'] = abs(high_case_sum_of_negatives)
        rr()
    # investments_details.loc[investments_details['Scenario'] == 'Low Case', 'Invested Amount'] = abs(low_case_sum_of_negatives)
    # investments_details.loc[investments_details['Scenario'] == 'Base case', 'Invested Amount'] = abs(base_case_sum_of_negatives)
    # investments_details.loc[investments_details['Scenario'] == 'High Case', 'Invested Amount'] = abs(high_case_sum_of_negatives)


    if not ss.investments_data.equals(investments_details_v2):
        # print('Antony')
        ss.investments_data = investments_details_v2

        max_date = ss.investments_data['Exit Date'].max()

        sample_data = ss.assumptions_data

        date_range = pd.date_range(start=min_date, end=max_date, freq='M')
        ss.assumptions_data = pd.DataFrame(date_range, columns=['Date'])
        ss.assumptions_data['Date'] = pd.to_datetime(ss.assumptions_data['Date'], format='%Y-%m-%d').dt.strftime('%Y-%m-%d')
        ss.assumptions_data[["Low Case" ,"Base Case" ,"High Case" ,"Comments"]] = None
        merged_df = pd.merge(ss.assumptions_data, sample_data, on=['Date'], suffixes=('_df1', '_df2'), how='left')

        print('llllllll', merged_df )

        # Update 'Salary' in df1 where 'Salary_df2' is not NaN (indicating a match)
        merged_df['Low Case'] = merged_df.apply(lambda row: row['Low Case_df2'] if not pd.isna(row['Low Case_df2']) else row['Low Case_df1'], axis=1)
        merged_df['Base Case'] = merged_df.apply(lambda row: row['Base Case_df2'] if not pd.isna(row['Base Case_df2']) else row['Base Case_df1'], axis=1)
        merged_df['High Case'] = merged_df.apply(lambda row: row['High Case_df2'] if not pd.isna(row['High Case_df2']) else row['High Case_df1'], axis=1)
        merged_df['Comments'] = merged_df.apply(lambda row: row['Comments_df2'] if not pd.isna(row['Comments_df2']) else row['Comments_df1'], axis=1)

        # Select final columns and drop duplicates
        ss.assumptions_data = merged_df[['Date', "Low Case" ,"Base Case" ,"High Case" ,"Comments"]].drop_duplicates()

        # ss.assumptions_data[["Low Case" ,"Base Case" ,"High Case" ,"Comments"]] = None
        
        ss.assumptions_data.loc[0, ["Low Case" ,"Base Case" ,"High Case"]] = [ -investments_at_entry ,-investments_at_entry ,-investments_at_entry]
        
        investment_update = ss.assumptions_data

        low_case_sum_of_negatives = investment_update[investment_update['Low Case'] < 0]['Low Case'].sum()
        base_case_sum_of_negatives = investment_update[investment_update['Base Case'] < 0]['Base Case'].sum()
        high_case_sum_of_negatives = investment_update[investment_update['High Case'] < 0]['High Case'].sum()

        ss.investments_data.loc[ss.investments_data['Scenario'] == 'Low Case', 'Invested Amount'] = abs(low_case_sum_of_negatives)
        ss.investments_data.loc[ss.investments_data['Scenario'] == 'Base case', 'Invested Amount'] = abs(base_case_sum_of_negatives)
        ss.investments_data.loc[ss.investments_data['Scenario'] == 'High Case', 'Invested Amount'] = abs(high_case_sum_of_negatives)

        rr()




    st.subheader(':blue[Valuation Waterfall Output:]')

    column_values_list = investments_details_v2['Scenario'].tolist()
    column_values_values = investments_details_v2['EBITDA at Exit'].tolist()
    column_values_values2 = investments_details_v2['Multiple at Exit'].tolist()

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


    # FUNCTIONS
    def calculate_equity(df, case):
        arr_rev_ebitda = df.loc[df['Calc'] == 'ARR /Rev /EBITDA', case].values[0]
        multiple = df.loc[df['Calc'] == 'Multiple', case].values[0]
        net_debt = df.loc[df['Calc'] == 'Net Debt', case].values[0]
        cash_flow_adj = df.loc[df['Calc'] == 'Cash flow adj', case].values[0]

        if isinstance(arr_rev_ebitda, list):
            arr_rev_ebitda = int(arr_rev_ebitda[0])
        if isinstance(multiple, list):
            multiple = int(multiple[0]) 

        net_debt = 0 if net_debt == None else net_debt
        cash_flow_adj = 0 if cash_flow_adj == None else cash_flow_adj
        a = int(arr_rev_ebitda * multiple)
        b = int(int(net_debt) + int(cash_flow_adj))
        result = a + b
        return result

    def calculate_value(df, case):
        equity = df.loc[df['Calc'] == 'Equity', case].values[0]
        ownership = df.loc[df['Calc'] == 'Ownership %', case].values[0]

        equity = 1 if equity == None else equity
        ownership = 1 if ownership == None else ownership
        return (int(equity) * int(ownership))


    def calculate_money_multiple(df, case):
        value = df.loc[df['Calc'] == 'Value', case].values[0]
        investments = df.loc[df['Calc'] == 'Investment', case].values[0]

        value = 1 if value == None else value
        investments = 1 if investments == None else investments

        return str(value / investments) + 'x'


    # with st.container(height=300, border=True, backgroundColor='red'):
    with st.container(height=300, border=True):
        st.write(data_v2)
        data_v3_edited_df = st.data_editor(data_v3)

        concatenated_df = pd.concat([data_v2, data_v3_edited_df], ignore_index=True)

        # Calculate Equity for each case
        equity_entry = calculate_equity(concatenated_df, 'Entry')
        equity_low_case = calculate_equity(concatenated_df, 'Low Case')
        equity_base_case = calculate_equity(concatenated_df, 'Base case')
        equity_high_case = calculate_equity(concatenated_df, 'High Case')

        equity_data = {
            'Calc': ['Equity'],
            'Entry':[equity_entry],
            'Low Case':[equity_low_case],
            'Base Case':[equity_base_case],
            'High Case':[equity_high_case]
        }

        equity_df = pd.DataFrame(equity_data)

        st.write(equity_df)

        ownership_data = {
            'Calc': ['Ownership %'],
            'Entry': None,
            'Low Case':None,
            'Base Case':None,
            'High Case':None
        }

        ownership_df = pd.DataFrame(ownership_data)

        # st.write(ownership_df)
        ownership_edited_df = st.data_editor(ownership_df)

        concatenated_df_v2 = pd.concat([equity_df, ownership_edited_df], ignore_index=True)

        # Calculate Equity for each case
        value_entry = calculate_value(concatenated_df_v2, 'Entry')
        value_low_case = calculate_value(concatenated_df_v2, 'Low Case')
        value_base_case = calculate_value(concatenated_df_v2, 'Base Case')
        value_high_case = calculate_value(concatenated_df_v2, 'High Case')


        value_and_investment = {
            'Calc': ['Value', 'Investment'],
            'Entry':[value_entry, investments_at_entry],
            'Low Case':[value_low_case, investments_at_entry],
            'Base Case':[value_base_case, investments_at_entry],
            'High Case':[value_high_case, investments_at_entry]
        }

        value_and_investment_df = pd.DataFrame(value_and_investment)
        st.write(value_and_investment_df)


            # Calculate Equity for each case
        money_multiple_entry = calculate_money_multiple(value_and_investment_df, 'Entry')
        money_multiple_low_case = calculate_money_multiple(value_and_investment_df, 'Low Case')
        money_multiple_base_case = calculate_money_multiple(value_and_investment_df, 'Base Case')
        money_multiple_high_case = calculate_money_multiple(value_and_investment_df, 'High Case')


        money_multiple = {
            'Calc': ['Money Multiple'],
            'Entry':[money_multiple_entry],
            'Low Case':[money_multiple_low_case],
            'Base Case':[money_multiple_base_case],
            'High Case':[money_multiple_high_case]
        }

        money_multiple_df = pd.DataFrame(money_multiple)
        st.write(money_multiple_df)


    st.subheader(':blue[Return Revenue:]')

    money_multiple_value = money_multiple_df.iloc[0].tolist()

    # IRR
    df3 = assumptions_edited_df_v2

    df3['Low Case'] = pd.to_numeric(df3['Low Case'], errors='coerce')
    df3['Base Case'] = pd.to_numeric(df3['Base Case'], errors='coerce')
    df3['High Case'] = pd.to_numeric(df3['High Case'], errors='coerce')

    # # Calculate days from the start date for each cash flow
    df3['Date'] = pd.to_datetime(df3['Date'])

    df3['Days'] = (df3['Date'] - df3['Date'].iloc[0]).dt.days

    # Adjusted cash flows considering time value of money
    df3['Low Case Cash Flow'] = df3['Low Case'] / (1 + 0.05)**(df3['Days'] / 365)
    df3['Low Case Cash Flow'] = df3['Low Case Cash Flow'].fillna(1)

    df3['Base Case Cash Flow'] = df3['Base Case'] / (1 + 0.05)**(df3['Days'] / 365)
    df3['Base Case Cash Flow'] = df3['Base Case Cash Flow'].fillna(1)

    df3['High Case Cash Flow'] = df3['High Case'] / (1 + 0.05)**(df3['Days'] / 365)
    df3['High Case Cash Flow'] = df3['High Case Cash Flow'].fillna(1)

    # Calculate IRR based on adjusted cash flows
    low_case_irr = npf.irr(df3['Low Case Cash Flow'])
    base_case_irr = npf.irr(df3['Low Case Cash Flow'])
    high_case_irr = npf.irr(df3['Low Case Cash Flow'])

    revenue_return = {
        'Return (calculated)': money_multiple_value[2:],
        'IRR (calculated)': [low_case_irr, base_case_irr, high_case_irr ]
    }
    revenue_return_df = pd.DataFrame(revenue_return)

    st.write(revenue_return_df)


if __name__ == '__main__':
    main()