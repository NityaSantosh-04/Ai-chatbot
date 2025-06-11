import string

class ResponseGenerator:
    def __init__(self, faq_data):
        self.faq_data = faq_data

    def normalize(self, text):
        return text.lower().translate(str.maketrans('', '', string.punctuation)).strip()

    def generate_response(self, user_input):
        normalized_input = self.normalize(user_input)
        for question, answer in self.faq_data.items():
            if self.normalize(question) in normalized_input:
                return answer
        return "I'm sorry, I don't have an answer for that. Please check back later."