from flask import Flask, request, jsonify, render_template
from chatbot.response_generator import ResponseGenerator

app = Flask(__name__)

# Add your FAQ data here
faq_data = {
    "what is your name": "I am an AI chatbot.",
    "how do I apply": "You can apply through our website.",
    "what is the internship duration": "The internship lasts for 3 months.",
    "what is the eligibility": "Any undergraduate student can apply."
}

response_generator = ResponseGenerator(faq_data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = response_generator.generate_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)