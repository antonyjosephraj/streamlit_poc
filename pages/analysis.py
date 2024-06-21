import pandas as pd
import numpy as np
import streamlit as st

import numpy_financial as npf

# Example DataFrame with dates and cash flows
# data = {
#     'Date': pd.to_datetime(['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01']),
#     'Cash Flow': [-100, 20, 30, 40]  # Negative for investment, positive for returns
# }
# df = pd.DataFrame(data)

# # Calculate days from the start date for each cash flow
# df['Days'] = (df['Date'] - df['Date'].iloc[0]).dt.days

# # Adjusted cash flows considering time value of money
# df['Adjusted Cash Flow'] = df['Cash Flow'] / (1 + 0.05)**(df['Days'] / 365)

# # Calculate IRR based on adjusted cash flows
# irr = npf.irr(df['Adjusted Cash Flow'])

# print(f"IRR: {irr:.2%}")
# st.write(df)

# st.write(irr)

from streamlit import session_state as ss, data_editor as de, rerun as rr
import pandas as pd


start_data = {'A': [None, None], 'B': [3, 8], 'C': [None, None]}


if 'start_df' not in ss:
    ss.start_df = pd.DataFrame(start_data)
    ss.start_df['A'] = pd.to_numeric(ss.start_df['A'], errors='coerce').astype('Int64')


def main():
    edited_df = de(ss.start_df, num_rows='dynamic')

    if not ss.start_df.equals(edited_df):
        ss.start_df = edited_df
        ss.start_df.loc[ss.start_df['A'].notna(), 'C'] = ss.start_df['A'] + ss.start_df['B']
        rr()


if __name__ == '__main__':
    main()