// cambia esto por tu ip local
const IP = "192.168.1.35";

const ws = new WebSocket(`ws://${IP}:8080`);

ws.onopen = function(event) {
    console.log('Connected to WebSocket server');
};
function sendMessage(message) {
    ws.send(message);
}
function changePage() {
    // Apaga todos los leds para un nuevo archivo
    sendMessage("finish");
    window.location.href = "http://127.0.0.1:5001"; 
}