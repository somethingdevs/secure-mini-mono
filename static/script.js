var logs = document.getElementById('logs');
var messageInput = document.getElementById('message');

// Define the 'send' button
var sendButton = document.getElementById('send');


async function pollData() {
    const f = await fetch("http://localhost:8000/polling/data", {
        method: "GET",
    });
    const response = await f.json();
    logs.innerHTML = response['message'];
    logs.scrollTop = logs.scrollHeight;
}



async function sendData(data) {
    const f = await fetch("http://localhost:8000/polling/data", {
        method: "POST",
        body: {}
    });
}

sendButton.addEventListener('click', async (e) => {
    const value = messageInput.value;
    await fetch("http://localhost:8000/player_turn", {
        method: "POST",
        body: JSON.stringify({'text': value}),
        headers: {'Content-Type': 'application/json'}
    })
})

setInterval(pollData, 1000);