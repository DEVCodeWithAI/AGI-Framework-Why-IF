import streamlit as st

def primary_button(label, key):
    return st.button(label, key=key, use_container_width=True)

def secondary_button(label, key):
    return st.button(label, key=key, use_container_width=True, help="Click to proceed")
