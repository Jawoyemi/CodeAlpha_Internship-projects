#basic chatbot functionality
def chatbot():
    rules = {
        "hello": "Hi!",
        "hi": "Hello!",
        "how are you": "I'm fine.",
        "bye": "Goodbye!",
        "goodbye": "See you!"
    }
    print("Welcome to the chatbot!")
    print("Type 'bye' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input in rules:
            print(f"Chatbot: {rules[user_input]}")
            if user_input == "bye":
                break
        else:
            print("Chatbot: I don't understand that. Can you try again?")      
chatbot()