print("🤖 Welcome! I am Onyx.")
print("Type 'bye' to end the chat.\n")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("Onyx: Hello! Nice to meet you.")

    elif "how are you" in user:
        print("Onyx: I'm doing great! What about you?")

    elif "your name" in user:
        print("Onyx: I'm Onyx, your Python chatbot.")

    elif "help" in user:
        print("Onyx: You can say hi, ask my name, or ask how I am.")

    elif user == "bye":
        print("Onyx: Goodbye! Have a great day 👋")
        break

    else:
        print("Onyx: Sorry, I don't understand that yet.")