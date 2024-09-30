from flask import Flask, jsonify, request
from flask_cors import CORS
import spacy

app = Flask(__name__)
CORS(app)
nlp = spacy.load("en_core_web_sm")
text_messages = []
token_list = []
name = "littlebot"

# The route for processing user message and response
@app.route('/message_input', methods=['GET', 'POST'])
def message_input():
    if request.method == 'POST':
        message = request.get_json()
        text = message['text']
        text_messages.append(text)
        return jsonify({"status": "Message received"}), 200
    elif request.method == 'GET':
        if text_messages:
            text = text_messages[-1]  # Get the last message for demonstration
            return jsonify({"response": token_response(text)})
        else:
            return jsonify({"response": "No messages received yet"}), 200

# Code for string recognition
def token_response(text):
    doc = nlp(text)
    tokens = [token.text for token in doc]
    return " ".join(tokens)

if __name__ == '__main__':
    app.run(debug=True)
