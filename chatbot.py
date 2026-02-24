# Simple Rule-Based Chatbot

print("Hello! I am a simple chatbot.")
print("Type 'exit' to end the conversation.\n")

while True:
    user_input = input("You: ").lower()   # convert to lowercase

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hi there! How can I help you?")
    
    elif user_input == "how are you":
        print("Bot: I'm just a program, but I'm doing great!")
    
    elif user_input == "what is your name":
        print("Bot: I am a rule-based chatbot.")
    
    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break   # exit loop
    
    elif user_input == "exit":
        print("Bot: Exiting the chat. Bye!")
        break
    
    else:
        print("Bot: Sorry, I don't understand that.")
