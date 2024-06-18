from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='static')

# Predefined Q&A pairs
qa_pairs = {
    "what is your name": "I am a simple Q&A chatbot.",
    "how are you": "I'm just a bunch of code, but I'm doing great! How can I assist you?",
    "what can you do": "I can answer simple questions. Try asking me something!",
    "who created you": "I was created by a developer using Flask and Python.",
    "what is flask": "Flask is a micro web framework written in Python.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "what is the weather like": "I'm not connected to a weather service right now, so I can't provide that information.",
    "how can I optimize performance": "To optimize performance, you can look into improving your application's efficiency, reducing resource usage, and ensuring your infrastructure is scalable.",
    "what is kubernetes": "Kubernetes is an open-source system for automating the deployment, scaling, and management of containerized applications.",
    "goodbye": "Goodbye! Have a great day!"
}

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get('message', '').strip().lower()
    response = qa_pairs.get(user_input, "I don't understand that question. Can you please ask something else?")
    return jsonify({'response': response})

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
