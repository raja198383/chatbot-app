from flask import Flask, request, jsonify

app = Flask(__name__)

# Predefined Q&A pairs
qa_pairs = {
    "what is your name": "I am a simple Q&A chatbot.",
    "how are you": "I'm just a bunch of code, but I'm doing great! How can I assist you?",
    "what can you do": "I can answer simple questions. Try asking me something!",
    "bye": "Goodbye! Have a great day!"
}

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get('message', '').strip().lower()
    response = qa_pairs.get(user_input, "I don't understand that question. Can you please ask something else?")
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
