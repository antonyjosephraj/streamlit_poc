import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np

st.subheader('REPORTING')

# plt.figure(figsize = (6, 6))
# colors = [“royalblue”,”green”,”green”,”red”,”red”,”red”,
#           “royalblue”, “red”, “red”, “red”, “royalblue”]
# fig = df.T[1:].max(axis = 1).plot(kind = “bar”,
#                                   bottom = df[“Base”],
#                                   width = 0.8,
#                                   color = colors)
# selected_patches = fig.patches[0], fig.patches[2], fig.patches[4]
# plt.legend(selected_patches,
#            [“Base value”, “Rise”, “Fall”],
#            loc = “upper right”)
# plt.title(“My electricity saving plan”)
# plt.ylabel(“kWh consumption”)
# plt.tight_layout()
