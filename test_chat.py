import requests

URL = "http://127.0.0.1:8000/chat"

print("🤖 Chatbot started (type 'quit' to exit)\n")

while True:
    msg = input("You: ")
    if msg.lower() in ["quit", "exit"]:
        break

    res = requests.post(URL, json={"message": msg})
    data = res.json()

    print(f"Bot: {data['response']}")
    print(f"(intent: {data['intent']} | confidence: {data['confidence']}%)\n")