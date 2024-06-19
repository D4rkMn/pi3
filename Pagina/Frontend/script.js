// cambia esto por tu ip local
const IP = "192.168.1.39";

const ws = new WebSocket(`ws://${IP}:8080`);

ws.onopen = function(event) {
    console.log('Connected to WebSocket server');
};

ws.onmessage = function(event) {
    console.log('Message from server: ' + event.data);
};

function sendMessage(message) {
    ws.send(message);
}