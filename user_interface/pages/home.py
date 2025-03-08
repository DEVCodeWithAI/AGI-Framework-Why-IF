import streamlit as st
from components.sidebar import sidebar
from components.navbar import navbar

def home():
    navbar()
    
    st.markdown("## 👋 Welcome to Why & IF Framework")
    st.markdown("Control panel for managing the AI framework.")

    # AI Interaction Section
    st.markdown("### 🤖 AI Interaction")
    st.write("Ask a question to the AI:")

    # Form nhập câu hỏi
    user_input = st.text_input("Enter your question...", placeholder="Ask me anything about Why & IF Framework...")
    if st.button("Submit", help="Click to ask AI"):
        st.success(f"AI is processing your question: {user_input}")

    # System Status Section
    st.markdown("### 🔍 System Status")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("✅ **AI Running**")
    with col2:
        st.markdown("⚡ **Model:** LLaMA 2-7B Fine-Tuned")
    with col3:
        st.markdown("📦 **Memory Bank Active**")

if __name__ == "__main__":
    page = sidebar()
    if page == "Home":
        home()
