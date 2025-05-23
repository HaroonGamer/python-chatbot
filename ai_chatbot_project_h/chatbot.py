import os
from dotenv import load_dotenv
from chat_engine import ChatEngine

load_dotenv()  # load API key from .env file

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY not found. Please add it to your .env file.")
        return

    chat = ChatEngine(api_key=api_key)
    print("Welcome to AI Chatbot! Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chat.ask(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
