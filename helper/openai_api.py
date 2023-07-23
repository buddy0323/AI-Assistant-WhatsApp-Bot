# Import the required modules
import os
import openai
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Get the OpenAI API key from the environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

def chat_complition(prompt: str) -> dict:
    '''
    Call Openai API for text completion
    Parameters:
        - prompt: user query (str)
    Returns:
        - dict
    '''
    try:
        # Create a chat completion with the OpenAI API
        # The model is set to 'gpt-3.5-turbo'
        # The system message sets the behavior of the assistant
        # The user message is the prompt we want the model to respond to
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {
                    'role': 'system',
                    'content': 'You are a helpful assistant.'
                },
                {
                    'role': 'user',
                    'content': prompt
                },
            ])

        # Print a success message with the response from the OpenAI API call
        print(f"OpenAI API call successful. Response: {response}")  

        # Return a dictionary with the status and the content of the response
        return {
            'status': 1,
            'response': response['choices'][0]['message']['content']
        }
    except Exception as e:
        # Print any error that occurs during the OpenAI API call
        print(f"OpenAI API call failed. Error: {e}")  

        # Return a dictionary with the status and an empty response
        return {'status': 0, 'response': ''}  
