import nltk
import random
import re
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

# Jokes
jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why was the math book sad? It had too many problems.",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats."
]

# Simulated weather
weather_conditions = [
    "It's sunny and bright ☀️",
    "Looks like it's going to rain 🌧️",
    "It's quite windy outside 🌬️",
    "It's a bit cloudy today ☁️",
    "Feels chilly and cold ❄️"
]

# Calculator
def handle_calculation(text):
    try:
        expression = re.sub(r'[^\d\.\+\-\*/\(\)]', '', text)
        if expression:
            result = eval(expression)
            return f"The answer is {result}"
    except:
        return "Sorry, I couldn't calculate that. Try a simpler expression."
    return "I didn't catch the numbers clearly. Try again."

# Custom intent-based responder
def custom_response(text):
    text = text.lower()

    if any(word in text for word in ["name", "your name", "who are you"]):
        return "You can call me Chatty! I'm your friendly Python chatbot 😊"

    if any(word in text for word in ["weather", "climate", "temperature", "rain"]):
        return random.choice(weather_conditions)

    if any(word in text for word in ["joke", "funny", "laugh"]):
        return random.choice(jokes)

    if any(word in text for word in ["calc", "calculate", "+", "-", "*", "/", "what is"]):
        return handle_calculation(text)

    if any(word in text for word in ["help", "what can you do", "features"]):
        return "I can tell jokes, do math, simulate weather, and have fun chats!"

    if any(word in text for word in ["bye", "exit", "goodbye", "see you"]):
        return random.choice(["Goodbye! 👋", "See you later!", "Bye! Have a great day!"])

    return None

# Default patterns
pairs = [
    [r"hi|hello|hey", ["Hello there!", "Hey! What's up?", "Hi! 😊"]],
    [r"how are you", ["I'm just code, but I'm doing great! What about you?"]],
    [r"(.*)", ["Hmm... I'm not sure about that, but I'm all ears!", 
               "Let's talk more — ask me about weather, jokes, or math!", 
               "Interesting! Try asking about something fun like a joke!"]],
]

# Smart chatbot class
class SmartChat(Chat):
    def respond(self, str):
        intent = custom_response(str)
        if intent:
            return intent
        else:
            return super().respond(str)

# Start chatbot
chatbot = SmartChat(pairs, reflections)

print("Hi! I'm Chatty 🤖 — Ask me about weather, math, jokes, or just say hi!\nType 'bye' to end.\n")
chatbot.converse()
