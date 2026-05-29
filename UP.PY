print("Simple Chat Bot")

while True:
    message = input("\nYou: ").lower()

    if message == "hello":
        print("Bot: Hi")

    elif message == "how are you":
        print("Bot: I am fine")

    elif message == "your name":
        print("Bot: My name is Python Bot")

    elif message == "bye":
        print("Bot: Goodbye")
        break

    else:
        print("Bot: I do not understand")