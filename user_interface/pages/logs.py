import streamlit as st
from components.sidebar import sidebar
from components.navbar import navbar

def logs():
    navbar()
    st.title("📜 AI Logs")
    st.write("View system logs and AI activity.")

    # Hiển thị log file giả lập
    logs = ["[INFO] AI started...", "[INFO] Model loaded successfully.", "[WARNING] Memory usage high."]
    for log in logs:
        st.code(log)

if __name__ == "__main__":
    page = sidebar()
    if page == "Logs":
        logs()
