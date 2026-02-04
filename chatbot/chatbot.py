print("Chatbot running... (type 'exit' to stop)")

greetings = ["hello", "hi", "hey"]
farewell = ["bye", "goodbye"]

while True:
    text = input("\nYou: ").lower()

    if text == "exit":
        print("Bot: Chat ended.")
        break

    elif any(word in text for word in greetings):
        print("Bot: Hello! How can I help you?")

    elif "name" in text:
        print("Bot: I am a Python chatbot.")

    elif "how are you" in text:
        print("Bot: I'm doing well!")

    elif any(word in text for word in farewell):
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: I don't understand that.")


