import chromadb
from sentence_transformers import SentenceTransformer
from database import get_or_create_collection  # Import function from database.py

# Initialize ChromaDB
collection = get_or_create_collection()  # Ensure collection exists before accessing

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_knowledge(query, top_k=3):
    """Finds the most relevant knowledge from the database."""
    query_vector = embedding_model.encode(query).tolist()
    results = collection.query(query_embeddings=[query_vector], n_results=top_k)

    # Ensure the results contain documents
    if results and results.get("documents") and results["documents"][0]:
        return [doc["text"] for doc in results["documents"][0] if doc]
    
    return ["I don't have information on that yet. Please provide some context!"]

if __name__ == "__main__":
    print(retrieve_knowledge("What is AI?"))
