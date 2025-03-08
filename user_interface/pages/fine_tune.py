import streamlit as st
from components.sidebar import sidebar
from components.navbar import navbar

def fine_tune():
    navbar()
    st.title("🎯 Fine-Tuning AI")
    st.write("Adjust and improve the AI model.")

    st.file_uploader("Upload fine-tuning dataset (JSON/CSV)")
    st.button("Start Fine-Tuning")

if __name__ == "__main__":
    page = sidebar()
    if page == "Fine-Tune":
        fine_tune()
