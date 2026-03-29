import streamlit as st
import requests
import re
import os

st.set_page_config(page_title="Text Summarizer")

st.title("Text Summarizer")
st.subheader("using HuggingFace Transformer")

HF_API_KEY = st.secrets["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"]
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

def clean_data(text):
    text = re.sub(r"\r\n", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"<.*?>", " ", text)
    return text.strip()

def summarize(text):
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    result = response.json()
    if isinstance(result, list):
        return result[0]["summary_text"]
    return "Error: " + str(result)

text_input = st.text_area("Write or Paste your content below:", height=200)

if st.button("Summarize"):
    if text_input.strip():
        with st.spinner("Processing..."):
            cleaned = clean_data(text_input)
            summary = summarize(cleaned)
            st.success("Content Summary")
            st.write(summary)
    else:
        st.warning("Please enter some text!")
