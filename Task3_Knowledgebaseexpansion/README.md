# Task 3: Dynamic Chatbot with Knowledge Base Expansion

## Overview
This project implements a chatbot that dynamically expands its knowledge base using ChromaDB and generates responses with the Ollama "mistral" model.

The chatbot retrieves relevant knowledge from the vector database and uses it as context for Ollama's language model to generate meaningful replies.

---

## Folder Structure
- `chatbot.py` — Main chat interface integrating retrieval and Ollama.
- `database.py` — Handles ChromaDB initialization, knowledge insertion, update, and clearing.
- `retriever.py` — Retrieves top-k relevant knowledge entries for user queries.
- `ui.py` — Streamlit interface for chatting and adding knowledge.
- `data/` — Contains persistent ChromaDB and SQLite database files.
- `requirements.txt` — Required Python packages.

---

## Setup Instructions

1. Clone the repo.
2. Create a virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt
3.Ensure Ollama is installed and properly configured.

4.Run the Streamlit UI:

    streamlit run ui.py

How it works
User inputs a query.

The retriever.py fetches the most relevant knowledge from ChromaDB.

The query and retrieved context are sent to the Ollama model to generate a response.

Users can add new knowledge entries through the sidebar to dynamically expand the database.

Notes
The embedding model used is all-MiniLM-L6-v2 from Sentence Transformers.

Ollama model used: mistral.

Make sure data/ folder is accessible and has write permissions.

Ollama requires local installation or access — check Ollama documentation.