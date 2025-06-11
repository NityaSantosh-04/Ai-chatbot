# AI Chatbot Application

This project is an AI chatbot designed to respond to frequently asked questions about internships, application processes, and organization information. The chatbot utilizes natural language processing techniques to provide accurate and helpful responses to users.

## Project Structure

```
ai-chatbot-app
├── src
│   ├── main.py                # Entry point of the application
│   ├── chatbot
│   │   ├── __init__.py        # Initializes the chatbot package
│   │   ├── faq_data.py        # Contains FAQ data and functions to load it
│   │   ├── response_generator.py # Generates responses based on user input
│   │   └── utils.py           # Utility functions for various tasks
│   ├── static
│   │   ├── css
│   │   │   └── styles.css     # CSS styles for the chatbot interface
│   │   └── js
│   │       └── chatbot.js      # JavaScript for handling user interactions
│   └── templates
│       ├── index.html         # Main HTML page for user interaction
│       └── chat.html          # HTML structure for the chatbot interface
├── requirements.txt            # Lists project dependencies
└── README.md                   # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd ai-chatbot-app
   ```

2. **Install dependencies**:
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Start the chatbot server by running:
   ```
   python src/main.py
   ```

4. **Access the chatbot**:
   Open your web browser and navigate to `http://localhost:5000` to interact with the chatbot.

## Usage Guidelines

- The chatbot is designed to assist users with common queries related to internships and the application process.
- Users can type their questions in the chat interface, and the chatbot will provide relevant answers based on the FAQ data.

## Capabilities

- Responds to frequently asked questions.
- Provides information about the organization and application processes.
- Utilizes natural language processing for better understanding of user queries.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.