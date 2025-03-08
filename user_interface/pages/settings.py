import streamlit as st
from components.sidebar import sidebar
from components.navbar import navbar

def settings():
    navbar()
    st.title("⚙ Settings")
    st.write("Configure the AI framework.")

    # Tùy chỉnh cài đặt hệ thống
    st.checkbox("Enable Debug Mode")
    st.slider("Adjust AI Sensitivity", min_value=1, max_value=10, value=5)
    st.selectbox("Choose Model", ["LLaMA 2-7B", "LLaMA 13B", "Mistral 7B", "GPT-4"])

if __name__ == "__main__":
    page = sidebar()
    if page == "Settings":
        settings()
