# Import the required modules
from flask import Flask, request, jsonify
from helper.openai_api import chat_complition
from helper.twilio_api import send_message

# Create a Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    # Return a JSON response with the status, webhook URL, message, and video URL
    return jsonify(
        {
            'status': 'OK',
            'wehook_url': 'BASEURL/twilio/receiveMessage',
            'message': 'The webhook is ready.',
            'video_url': 'https://youtu.be/y9NRLnPXsb0'
        }
    )

# Define the route for receiving messages from Twilio
@app.route('/twilio/receiveMessage', methods=['POST'])
def receiveMessage():
    try:
        # Extract incoming parameters from Twilio
        message = request.form['Body']
        sender_id = request.form['From']

        # Print the received message and sender id
        print(f"Received message: {message} from {sender_id}")  

        # Get response from OpenAI
        result = chat_complition(message)

        # Print the response from OpenAI
        print(f"OpenAI response: {result}")  

        # If the OpenAI response was successful, send the response as a message to the sender
        if result['status'] == 1:
            send_message(sender_id, result['response'])
    except Exception as e:
        # Print any error that occurs
        print(f"Error: {e}")  
    # Return a 200 OK response
    return 'OK', 200
