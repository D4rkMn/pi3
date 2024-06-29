// cambia esto por tu ip local
const IP = "localhost";

const ws = new WebSocket(`ws://${IP}:8080`);

ws.onopen = function(event) {
    console.log('Connected to WebSocket server');
};
function sendMessage(message) {
    ws.send(message);
}

