# FAQ data for the chatbot

faq_data = {
    "internships": {
        "questions": [
            "What internships do you offer?",
            "How can I apply for an internship?",
            "What are the eligibility criteria for internships?"
        ],
        "answers": [
            "We offer internships in various fields including software development, marketing, and design.",
            "You can apply for an internship by filling out the application form on our website.",
            "Eligibility criteria vary by internship, but generally, you should be a student or recent graduate."
        ]
    },
    "application_process": {
        "questions": [
            "What is the application process?",
            "How long does it take to get a response?",
            "Can I apply for multiple positions?"
        ],
        "answers": [
            "The application process involves submitting your resume and cover letter, followed by an interview.",
            "You can expect a response within 2-4 weeks after submitting your application.",
            "Yes, you can apply for multiple positions, but please ensure you meet the qualifications for each."
        ]
    },
    "organization_info": {
        "questions": [
            "What is MITS?",
            "What values does MITS uphold?",
            "How can I learn more about MITS?"
        ],
        "answers": [
            "MITS is an organization focused on innovation and technology solutions.",
            "We uphold values such as integrity, collaboration, and excellence.",
            "You can learn more about MITS by visiting our website or following us on social media."
        ]
    }
}

def get_faq_data():
    return faq_data

def get_questions(category):
    return faq_data.get(category, {}).get("questions", [])

def get_answer(category, question):
    questions = faq_data.get(category, {}).get("questions", [])
    answers = faq_data.get(category, {}).get("answers", [])
    if question in questions:
        index = questions.index(question)
        return answers[index]
    return "I'm sorry, I don't have an answer for that question."