// Connect to the WebSocket endpoint
var ws = new WebSocket("ws://127.0.0.1:8000/ws");

// Define the 'logs' textarea and the 'message' input field
var logs = document.getElementById('logs');
var messageInput = document.getElementById('message');

// Define the 'send' button
var sendButton = document.getElementById('send');

// When a message is received from the server, append it to the 'logs' textarea
ws.onmessage = function(event) {
    logs.value += event.data + '\n';
};

// When the 'send' button is clicked, send the content of the 'message' input field to the server
sendButton.addEventListener('click', function(event) {
    ws.send(messageInput.value);
    messageInput.value = '';
});