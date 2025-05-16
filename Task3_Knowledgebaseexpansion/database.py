import chromadb
from sentence_transformers import SentenceTransformer

# Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path="./data/chromadb/")

# Ensure collection exists before using it
def get_or_create_collection():
    try:
        return chroma_client.get_collection(name="chatbot_knowledge")
    except chromadb.errors.InvalidCollectionException:
        return chroma_client.create_collection(name="chatbot_knowledge")

collection = get_or_create_collection()

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def add_knowledge(text, source):
    """Embeds and adds new knowledge to the vector database."""
    vector = embedding_model.encode(text).tolist()
    collection.add(ids=[source], embeddings=[vector], metadatas=[{"text": text, "source": source}])

def get_all_knowledge():
    """Returns all stored knowledge from the database."""
    return collection.get()

def update_knowledge(text, source):
    """Updates an existing knowledge entry."""
    collection.delete(ids=[source])
    add_knowledge(text, source)

def clear_database():
    """Deletes all stored knowledge (for debugging)."""
    collection.delete(where={})

if __name__ == "__main__":
    print("Knowledge Base Ready!")
