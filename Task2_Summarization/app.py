import streamlit as st
import nltk
nltk.data.path.append("C:/Users/devan/nltk_data")
from summarizer import extractive_summary




st.title("Extractive Text Summarization")

# Input Text
text = st.text_area("Enter your text:", height=200)

# Number of sentences in summary
num_sentences = st.slider("Number of sentences in summary:", 1, 10, 3)

# Generate Summary
if st.button("Summarize"):
    if text:
        summary = extractive_summary(text, num_sentences)
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter text to summarize.")
