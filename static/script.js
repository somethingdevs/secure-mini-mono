var logs = document.getElementById('logs');
var messageInput = document.getElementById('message');
const room_id = "{{ room_id }}";

let room_id_val = window.location.href.split('/')[4]

console.log('Room = ', room_id);

// Define the 'send' button
var sendButton = document.getElementById('send');

async function pollData() {

    console.log('ee1', room_id_val)
    const f = await fetch(`https://localhost:8000/polling/data?room_id=${room_id_val}`, {
        method: "GET",
    });
    const response = await f.json();
    logs.innerHTML = response['message'];
    logs.scrollTop = logs.scrollHeight;
}



async function sendData(data) {
    const f = await fetch("https://localhost:8000/polling/data", {
        method: "POST",
        body: {}
    });
}

sendButton.addEventListener('click', async (e) => {
    const value = messageInput.value;
    await fetch(`https://localhost:8000/player_turn?room_id=${room_id_val}`, {
        method: "POST",
        body: JSON.stringify({'text': value}),
        headers: {'Content-Type': 'application/json'}
    })
})

setInterval(pollData, 1000);