from flask import Flask, request, jsonify, send_from_directory
import pyttsx3
import speech_recognition as sr
import threading
import queue

app = Flask(__name__)

# Create a queue for speech requests
speech_queue = queue.Queue()

def speak():
    engine = pyttsx3.init()
    while True:
        text = speech_queue.get()
        if text is None:
            break
        engine.say(text)
        engine.runAndWait()

def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.7
        try:
            audio = r.listen(source, timeout=5)
            query = r.recognize_google(audio)
            return query
        except Exception as e:
            return str(e)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/command', methods=['POST'])
def command():
    try:
        action = request.json.get('action')
        print(f"Action received: {action}")  # Debug print
        if action == 'listen':
            query = take_commands()
            print(f"Query recognized: {query}")  # Debug print
            return jsonify({'response': query})
        elif action == 'speak':
            text = request.json.get('text')
            speech_queue.put(text)
            return jsonify({'response': 'Speaking done'})
        else:
            return jsonify({'response': 'Invalid action'})
    except Exception as e:
        return jsonify({'response': f'Error: {str(e)}'})


if __name__ == '__main__':
    threading.Thread(target=speak, daemon=True).start()
    app.run(debug=True)
    
