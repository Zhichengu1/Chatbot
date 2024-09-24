from flask import Flask, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "methods": ["POST"]}})

# Initialize the ChatBot
chatbot = ChatBot('MyChatBot')

# Train the ChatBot (you can do this separately and save the model)
trainer = ListTrainer(chatbot)
trainer.train([
    "Hi, how are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you.",
    "You're welcome."
])

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/send_messages', methods=['POST'])
def messages():
    try:
        data = request.get_json()
        logging.info(f"Received data: {data}")
        
        if data is None:
            logging.error("No data received")
            return jsonify({'error': 'No data received'}), 400
        
        message = data.get('message')
        logging.info(f"Message: {message}")
        
        if not message:
            logging.error("No message found in data")
            return jsonify({'error': 'No message found in data'}), 400
        
        # Get response from the chatbot
        response = chatbot.get_response(message)
        logging.info(f"Chatbot response: {response}")
        return jsonify({'response': str(response)})
    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({'error': 'An error occurred'}), 500


if __name__ == '__main__':
    app.run(debug=True)
