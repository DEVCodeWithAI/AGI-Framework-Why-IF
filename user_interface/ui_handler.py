import streamlit as st
from components.sidebar import sidebar
from pages.home import home
from pages.fine_tune import fine_tune
from pages.logs import logs
from pages.settings import settings

st.set_page_config(page_title="Why & IF Framework", layout="wide")

page = sidebar()

if page == "Home":
    home()
elif page == "Fine-Tune":
    fine_tune()
elif page == "Logs":
    logs()
elif page == "Settings":
    settings()
