from flask import Flask, jsonify, request
from flask_cors import CORS
import spacy, emoji

app = Flask(__name__)
CORS(app)
nlp = spacy.load("en_core_web_sm") #load standard language english
text_messages = []
token_list = []

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






#routes for other purposes







 
 
 
 












#fucntions
# Code for string recognition
def token_response(text):
    doc = nlp(text)
    if text[-1] == '?':  # Check if the last character of the text is a question mark
        return "I don't know"
    return "my name i"




# read file and print the emoji
def read_emoji():
    return " no emoji find"



# math solver
def math_solver() -> int:
    return 0


#interactive disscussion
def disscussion() -> str:
    return "i like"
    
#give back url





if __name__ == '__main__':
    app.run(debug=True)
