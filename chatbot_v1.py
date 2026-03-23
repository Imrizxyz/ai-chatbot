while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi!")

    elif user == "how are you":
        print("Bot: I'm good 😄")

    elif user == "bye":
        print("Bot: Bye! 👋")
        break

    else:
        print("Bot: I don't understand")
