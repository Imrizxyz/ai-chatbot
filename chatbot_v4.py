from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

while True:
    user = input("You: ")

    if user.lower() == "bye":
        print("Bot: Bye! 👋")
        break

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": user}
        ]
    )

    reply = response.choices[0].message.content
    print("Bot:", reply)
