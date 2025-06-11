const chatbotContainer = document.getElementById('chatbot-container');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');
const chatLog = document.getElementById('chat-box');

sendButton.addEventListener('click', sendMessage);
userInput.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

function sendMessage() {
    const message = userInput.value;
    if (message.trim() === '') return;

    appendMessage('User', message);
    userInput.value = '';

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message }),
    })
    .then(response => response.json())
    .then(data => {
        appendMessage('Bot', data.response);
    })
    .catch(error => {
        console.error('Error:', error);
        appendMessage('Bot', 'Sorry, something went wrong. Please try again later.');
    });
}

function appendMessage(sender, message) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message');
    messageElement.classList.add(sender.toLowerCase());
    messageElement.textContent = `${sender}: ${message}`;
    chatLog.appendChild(messageElement);
    chatLog.scrollTop = chatLog.scrollHeight; // Scroll to the bottom
}