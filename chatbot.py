import pandas as pd
import numpy as np

# Load FAQs
faq_df = pd.read_csv("data/faq.csv")

def get_intent(user_input):
    # Basic matching by keyword presence
    for intent in faq_df["intent"].unique():
        if intent in user_input.lower():
            return intent
    return None

def respond(user_input):
    user_input = user_input.lower()

    # Try exact or partial match with question column
    matches = faq_df[faq_df['question'].apply(lambda q: q.lower() in user_input or user_input in q.lower())]

    if not matches.empty:
        return np.random.choice(matches["response"].values)
    else:
        return "Sorry, I don't understand that. Try asking something else."


def run_chatbot():
    print("Welcome to the Mini AI Chatbot! (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Bot: Goodbye!")
            break
        reply = respond(user_input)
        print(f"Bot: {reply}")

if __name__ == "__main__":
    run_chatbot()
