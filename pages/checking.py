import streamlit as st

HORIZONTAL_RED = "images/jman-logo.png"
ICON_RED = "images/jman-logo2.jpg"
HORIZONTAL_BLUE = "images/horizontal_blue.png"
ICON_BLUE = "images/icon_blue.png"

options = [HORIZONTAL_RED, ICON_RED]
sidebar_logo = st.selectbox("Sidebar logo", options, 0)

main_body_logo = st.selectbox("Main body logo", options, 1)

st.logo(sidebar_logo, icon_image=main_body_logo)
st.sidebar.markdown("Hi!")

