import ollama
from retriever import retrieve_knowledge

def chat_with_bot(user_input):
    """Fetches relevant data and uses Ollama for response generation."""
    context = retrieve_knowledge(user_input)
    prompt = f"User: {user_input}\nContext: {context}\nChatbot:"

    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        print("Bot:", chat_with_bot(user_input))
