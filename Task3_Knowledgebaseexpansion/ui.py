import streamlit as st
from chatbot import chat_with_bot
from database import add_knowledge

st.title("💬 Dynamic Chatbot with Expanding Knowledge")

user_input = st.text_input("Ask me anything:", "")

if user_input:
    response = chat_with_bot(user_input)
    st.write(f"🤖 Chatbot: {response}")

with st.sidebar:
    st.header("📚 Add Knowledge")
    new_text = st.text_area("New Knowledge Text:")
    new_source = st.text_input("Source/ID:")

    if st.button("Add to Knowledge Base"):
        if new_text and new_source:
            add_knowledge(new_text, new_source)
            st.success("Knowledge Added!")
        else:
            st.error("Please fill in both fields.")

st.write("💡 This chatbot dynamically updates its knowledge base using ChromaDB.")
