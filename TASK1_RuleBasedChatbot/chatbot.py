import random
import time
from datetime import datetime
from responses import responses


def bot_reply(message):
    print("\nBot: ", end="")
    for letter in message:
        print(letter, end="", flush=True)
        time.sleep(0.02)
    print()


def save_chat(user_message, bot_message):
    with open("chat_history.txt", "a", encoding="utf-8") as file:
        file.write(f"You: {user_message}\n")
        file.write(f"Bot: {bot_message}\n\n")


print("=" * 60)
print("🤖 RULEBOT")
print("Rule-Based AI Chatbot")
print("Developed for CodSoft AI Internship")
print("=" * 60)
print("Type 'help' to see available commands.")
print("Type 'bye' to exit.")
print("=" * 60)

while True:

    user = input("\nYou: ").strip().lower()

    if user in responses["greetings"]:
        reply = random.choice(responses["greetings"][user])
        bot_reply(reply)
        save_chat(user, reply)

    elif "how are you" in user:
        reply = responses["how are you"]
        bot_reply(reply)
        save_chat(user, reply)

    elif "your name" in user or "who are you" in user:
        reply = responses["name"]
        bot_reply(reply)
        save_chat(user, reply)

    elif "who created you" in user or "creator" in user:
        reply = responses["creator"]
        bot_reply(reply)
        save_chat(user, reply)

    elif "python" in user:
        reply = responses["python"]
        bot_reply(reply)
        save_chat(user, reply)

    elif "artificial intelligence" in user or "what is ai" in user or user == "ai":
        reply = responses["ai"]
        bot_reply(reply)
        save_chat(user, reply)

    elif "machine learning" in user or user == "ml":
        reply = responses["ml"]
        bot_reply(reply)
        save_chat(user, reply)

    elif "nlp" in user:
        reply = responses["nlp"]
        bot_reply(reply)
        save_chat(user, reply)

    elif "time" in user:
        reply = datetime.now().strftime("%I:%M:%S %p")
        bot_reply(reply)
        save_chat(user, reply)

    elif "date" in user:
        reply = datetime.now().strftime("%d-%m-%Y")
        bot_reply(reply)
        save_chat(user, reply)

    elif "joke" in user:
        reply = responses["joke"]
        bot_reply(reply)
        save_chat(user, reply)

    elif "motivate" in user or "motivation" in user:
        reply = responses["motivation"]
        bot_reply(reply)
        save_chat(user, reply)

    elif "quote" in user:
        reply = responses["quote"]
        bot_reply(reply)
        save_chat(user, reply)

    elif "weather" in user:
        reply = responses["weather"]
        bot_reply(reply)
        save_chat(user, reply)

    elif "food" in user:
        reply = responses["food"]
        bot_reply(reply)
        save_chat(user, reply)

    elif "favorite color" in user:
        reply = responses["favorite color"]
        bot_reply(reply)
        save_chat(user, reply)

    elif "thank" in user:
        reply = responses["thank you"]
        bot_reply(reply)
        save_chat(user, reply)

    elif "sorry" in user:
        reply = responses["sorry"]
        bot_reply(reply)
        save_chat(user, reply)

    elif "help" in user:
        reply = responses["help"]
        bot_reply(reply)
        save_chat(user, reply)

    elif user in ["bye", "exit", "goodbye"]:
        reply = responses["bye"]
        bot_reply(reply)
        save_chat(user, reply)
        break

    else:
        reply = "Sorry, I don't understand that. Type 'help' to see available commands."
        bot_reply(reply)
        save_chat(user, reply)