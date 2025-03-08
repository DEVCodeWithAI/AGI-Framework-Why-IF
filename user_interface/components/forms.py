import streamlit as st

def fine_tune_form():
    st.subheader("Fine-Tune AI Model")
    dataset = st.file_uploader("Upload Dataset (JSON, CSV)", type=["json", "csv"])
    model_selection = st.selectbox("Choose Base Model", ["LLaMA 2-7B", "Mistral 7B", "GPT4All"])
    learning_rate = st.slider("Learning Rate", 0.0001, 0.01, 0.001)
    epochs = st.number_input("Number of Epochs", min_value=1, max_value=100, value=10)
    return dataset, model_selection, learning_rate, epochs
