
# main.py - AI-Powered Chatbot Core Logic

import random

class NLUProcessor:
    def __init__(self):
        self.intents = {
            "greet": ["hello", "hi", "hey"],
            "farewell": ["bye", "goodbye", "see ya"],
            "thank": ["thanks", "thank you"],
            "query_time": ["time", "what time is it"],
            "query_date": ["date", "what day is it"]
        }
        self.entities = {
            "location": ["city", "place", "here"]
        }

    def detect_intent(self, text):
        text = text.lower()
        for intent, keywords in self.intents.items():
            if any(keyword in text for keyword in keywords):
                return intent
        return "unknown"

    def extract_entities(self, text):
        extracted = {}
        text = text.lower()
        for entity_type, keywords in self.entities.items():
            for keyword in keywords:
                if keyword in text:
                    extracted[entity_type] = keyword
                    break
        return extracted

class Chatbot:
    def __init__(self, nlu_processor):
        self.nlu = nlu_processor
        self.responses = {
            "greet": ["Hello there!", "Hi, how can I help you?"],
            "farewell": ["Goodbye!", "See you later!"],
            "thank": ["You're welcome!", "No problem!"],
            "query_time": ["I'm sorry, I cannot tell the current time."],
            "query_date": ["I'm sorry, I cannot tell the current date."],
            "unknown": ["I'm not sure how to respond to that.", "Could you rephrase that?"],
        }

    def get_response(self, user_input):
        intent = self.nlu.detect_intent(user_input)
        entities = self.nlu.extract_entities(user_input)
        
        # Example of entity-aware response (simple)
        if intent == "query_time" and "location" in entities:
            return f"I can't tell the time in {entities['location']}, but I can try to answer other questions."

        return random.choice(self.responses.get(intent, self.responses["unknown"]))

if __name__ == "__main__":
    nlu_processor = NLUProcessor()
    chatbot = Chatbot(nlu_processor)

    print("Chatbot: Hello! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")

# This is a simple example. A real NLU would use machine learning models.
# Further development would include training data, more complex entity extraction,
# and integration with external APIs for dynamic information like time/date.
# The current code demonstrates basic intent recognition and response generation.
# It's designed to be easily extensible with more intents and entities.
# The NLUProcessor class can be replaced with a more sophisticated library like SpaCy or NLTK.
# The Chatbot class handles the conversation flow and selects appropriate responses.
# Error handling and logging would also be crucial in a production system.
# This script serves as a foundational component for building advanced conversational agents.
# It's a starting point for exploring the exciting world of AI-powered chatbots.
# The goal is to provide a clear, readable, and functional example for developers.
# More features like context management and dialogue state tracking can be added later.
# The current version focuses on demonstrating core NLU and response generation principles.
# It's a testament to the power of Python in AI development.
# The code is structured for modularity and ease of understanding.
# It's a great example for beginners and a solid base for advanced projects.
# The use of classes helps organize the code and makes it more maintainable.
# The random choice for responses adds a touch of human-like variability.
# This chatbot is a small step towards creating intelligent virtual assistants.
# It's a fun and educational project to work on.
# The possibilities for expansion are endless.
# Enjoy experimenting with this AI-powered chatbot!
