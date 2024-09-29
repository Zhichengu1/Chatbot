import spacy
import random
nlp = spacy.load("en_core_web_sm")
intents = {
    "greeting": ["Hello!", "Hi there!", "Hey!"],
    "goodbye": ["Goodbye!", "See you later!", "Bye!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"]
}
def get_intent(text):
    doc = nlp(text)
    for token in doc:
        if token.lemma_ in intents:
            return token.lemma_
    return "unknown"

def generate_response(intent):
    if intent in intents:
        return random.choice(intents[intent])
    else:
        return "I'm not sure how to respond to that."
    

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    intent = get_intent(user_input)
    response = generate_response(intent)
    print(f"Bot: {response}")
