import streamlit as st

APP_NAME = "Pay for news"


st.set_page_config(
    page_title=APP_NAME,
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title(APP_NAME)
