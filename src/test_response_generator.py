from chatbot.response_generator import ResponseGenerator

faq_data = {
    "what is your name?": "I am an AI chatbot.",
    "how do I apply?": "You can apply through our website."
}

generator = ResponseGenerator(faq_data)

user_input = input("Ask a question: ")
response = generator.generate_response(user_input)
print("Chatbot:", response)