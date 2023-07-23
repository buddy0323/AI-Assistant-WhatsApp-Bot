# Import the Flask application from the app module in the src directory
from src.app import app

# Check if this script is the main program
if __name__ == '__main__':
    # If it is, run the Flask application
    # The host is set to '0.0.0.0' to make the server publicly available
    # The port is set to 5000
    # Debug mode is enabled for easier development
    app.run(host='0.0.0.0', port=5000, debug=True)
