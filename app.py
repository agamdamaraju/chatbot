from flask import Flask, request, jsonify
from transformers import pipeline

import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

app = Flask(__name__)

chatbotModel = pipeline("text-generation", model="microsoft/Phi-3-mini-4k-instruct", trust_remote_code=True)
history = []

@app.route('/chatbot', methods=['POST'])
def chatbot():
    userInput = request.json.get('message')
    if not userInput:
        return jsonify({'response': 'No input recieved. Please feed me something'}), 400
    response = generate_response(userInput)    
    return jsonify({'response': response})

def generate_response(user_input):
    history.append({
        "role": "user",
        "content": user_input
    })
    result = chatbotModel(history, max_new_tokens=250, use_cache=False, num_return_sequences = 1)
    history.append({"role": "assistant", "content": result[0]['generated_text'][-1]['content']})
    return result[0]['generated_text'][-1]['content']

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
