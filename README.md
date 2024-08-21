# Voice Assistant

A web-based voice assistant application that utilizes speech recognition and text-to-speech functionalities. The application allows users to interact with the assistant via voice commands and provides responses through synthesized speech.

## Features

- **Voice Command Recognition**: Uses Google Speech Recognition to understand spoken commands.
- **Text-to-Speech**: Converts text responses into spoken words using the pyttsx3 library.
- **Web Interface**: Interact with the voice assistant through a simple web page.

## Technologies Used

- **Python**: Main programming language.
- **Flask**: Web framework to handle HTTP requests and serve the web application.
- **pyttsx3**: Text-to-speech conversion library.
- **speech_recognition**: Speech recognition library to interpret voice commands.
- **HTML/CSS/JavaScript**: Front-end technologies to build the web interface.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/azhar707/voice-assistant.git


# Navigate to the project directory:


      cd voice-assistant
# Create a virtual environment (optional but recommended):
      python -m venv venv
# Activate the virtual environment:

**On Windows:**
      venv\Scripts\activate
**On macOS/Linux:**
      source venv/bin/activate
# Install the required packages:
      pip install -r requirements.txt
# Usage
Run the Flask application:
   python app.py
 # Open your web browser and go to:
   http://127.0.0.1:5000

Interact with the voice assistant by clicking the buttons on the web page to listen to commands and speak responses.

# Contributing
Feel free to fork the repository, make changes, and submit pull requests. Contributions and feedback are welcome!

# License
This project is licensed under the MIT License. See the LICENSE file for more details.

# Acknowledgements
Flask for the web framework.
pyttsx3 for text-to-speech functionalities.
speech_recognition for speech recognition capabilities.
Google Speech Recognition API for recognizing spoken commands.
