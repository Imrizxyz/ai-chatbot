import random
while True:
    user = input("You: ").lower()

    if "hello" in user or "hi" in user:
        replies = ["Hi! 👋", "Hello bro 😎", "Hey there!"]
        print("Bot:", random.choice(replies))

    elif "how are you" in user:
        replies = ["I'm good 😄", "Doing great bro 🔥", "All good!"]
        print("Bot:", random.choice(replies))

    elif "your name" in user:
        print("Bot: I'm your AI assistant 🤖")

    elif "bye" in user:
        print("Bot: Bye! Take care 👋")
        break

    else:
        replies = [
            "I didn't get that 🤔",
            "Can you say that again?",
            "Not sure bro 😅"
        ]
        print("Bot:", random.choice(replies))
