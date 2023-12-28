import streamlit as st

APP_NAME = "Pay for news"


st.set_page_config(
    page_title=APP_NAME,
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title(APP_NAME)

with st.sidebar:
    v1 = st.number_input("Google search ad revenue", value=0.0)
    v2 = st.number_input("Fraction user demand", value=0.350)
    v3 = st.number_input(
        "Split share", value=0.50, help="split between platform and publisher"
    )

# st.write(inputs)
st.write(v1 * v2 * v3, "dollar")
