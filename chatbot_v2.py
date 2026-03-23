while True:
    user = input("You: ").lower()

    if "hello" in user or "hi" in user:
        print("Bot: Hi! 👋")

    elif "how are you" in user:
        print("Bot: I'm good 😄")

    elif "bye" in user:
        print("Bot: Bye! 👋")
        break

    else:
        print("Bot: I don't understand")
