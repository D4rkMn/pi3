#include <WiFi.h>
#include <WebServer.h>
#include <WebSocketsClient.h>

// for testing and debugging
const char* IP = "(local ip)";
const int PORT = 8080;

const char* SSID = "(ssid)";
const char* PASSWORD = "(password)";


const int LED = 4;



WebSocketsClient webSocket;


void webSocketEvent(WStype_t type, uint8_t * payload, size_t length) {
  switch (type) {
    case WStype_DISCONNECTED:
      Serial.println("Disconnected!");
      break;
    case WStype_CONNECTED:
      Serial.println("Connected to WebSocket server");
      webSocket.sendTXT("Hello Server");
      break;
    case WStype_TEXT:
      Serial.printf("Received: %s\n", payload);
      // Display received message (could be on an OLED, Serial Monitor, etc.)
      Serial.println("Message from server: " + String((char*)payload));
      break;
  }
}

void setup() {
  Serial.begin(9600);

  WiFi.begin(SSID, PASSWORD);

  Serial.println("Connecting to WiFi...");

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
  
  webSocket.begin(IP, PORT, "/");
  webSocket.onEvent(webSocketEvent);
  
  //pinMode(LED, OUTPUT);
}

void loop() {

  webSocket.loop();
  
}