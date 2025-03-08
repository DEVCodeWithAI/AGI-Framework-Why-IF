import streamlit as st

def apply_theme():
    st.markdown("""
    <style>
        body { background-color: #f5f5f5; }
        .stButton>button { background-color: #4CAF50; color: white; border-radius: 10px; }
        .stTextInput>div>div>input { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)
