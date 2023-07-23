# Import the required modules
import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Get the Twilio account SID and auth token from the environment variables
account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_TOKEN')

# Create a Twilio client using the account SID and auth token
client = Client(account_sid, auth_token)


def send_message(to: str, message: str) -> None:
    '''
    Send message to a WhatsApp user.
    Parameters:
        - to(str): recipient's WhatsApp number in this format: 'whatsapp:+919558515995'
        - message(str): text message to send
    Returns:
        - None
    '''

    try:
        # Check if the message exceeds the 1600 character limit
        if len(message) > 1600:
            # If it does, truncate the message
            message = message[:1600]

        # Use the Twilio client to send the message
        _ = client.messages.create(from_='whatsapp:+14155238886',
                                   body=message,
                                   to=to)
        
        # Print a success message with the recipient and the message sent
        print(f"Message sent to {to}. Message: {message}")  
    except Exception as e:
        # Print any error that occurs during message sending
        print(f"Message sending failed. Error: {e}")  
