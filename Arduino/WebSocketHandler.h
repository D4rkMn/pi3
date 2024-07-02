#ifndef WEBSOCKETHANDLER_H
#define WEBSOCKETHANDLER_H

#include <WiFi.h>
#include <WebServer.h>
#include <WebSocketsClient.h>

#include "Message.h"
#include "Global.h"

class WebSocketHandler {
private:

  static WebSocketsClient webSocket;

  // WebSocket host details
  char* IP;
  int PORT;

  // Internet connection details
  char* SSID;
  char* PASSWORD;

  // Current message array
  //
  // There are as many messages as there are slaves
  static Message currentMessages[Global::NUMBER_OF_SLAVES];

  WebSocketHandler(char* IP, int PORT, char* SSID, char* PASSWORD) {
    this->IP = IP;
    this->PORT = PORT;
    this->SSID = SSID;
    this->PASSWORD = PASSWORD;

    
    WiFi.begin(this->SSID, this->PASSWORD);

    while (WiFi.status() != WL_CONNECTED) {
      delay(1000);
      Serial.println("Connecting to WiFi...");
    }

    Serial.println("Connected to WiFi");
    
    webSocket.begin(this->IP, this->PORT, "/");
    webSocket.onEvent(WebSocketHandler::webSocketEvent);
  }

  static void webSocketEvent(WStype_t type, uint8_t* payload, size_t length) {
    switch (type) {
      case WStype_DISCONNECTED:
        Serial.println("Disconnected!");
        break;
      case WStype_CONNECTED:
        Serial.println("Connected to WebSocket server");
        // test message
        //WebSocketHandler::webSocket.sendTXT("Hello server");
        break;
      case WStype_TEXT:
        Serial.printf("Received: %s\n", payload);
        WebSocketHandler::parseResponse((char*)payload);
        break;
    }
  }

  // Given a response from the websockets host, it will be parsed and update the current message array
  static void parseResponse(char* response) {
    // TODO: do something to update the response

  }

public:

  ~WebSocketHandler() {
    if (IP) delete[] IP;
    if (SSID) delete[] SSID;
    if (PASSWORD) delete[] PASSWORD;
  }

  const Message* getMessageArray() const {
    return currentMessages;
  }

  void sendSignal(const char* signal) {
    webSocket.sendTXT(signal);
  }

  void loop() {
    webSocket.loop();
  }

  friend class WebSocketBuilder;
};

class WebSocketBuilder {
private:

  // WebSocket host details
  char* IP;
  int PORT;

  // Internet connection details
  char* SSID;
  char* PASSWORD;

public:

  WebSocketBuilder() {}

  WebSocketBuilder& setHost(const char* IP, int PORT) {
    this->IP = new char[strlen(IP) + 1];
    strcpy(this->IP, IP);
    this->PORT = PORT;
    return *this;
  }

  WebSocketBuilder& setWiFi(const char* SSID, const char* PASSWORD) {
    this->SSID = new char[strlen(SSID) + 1];
    strcpy(this->SSID, SSID);

    this->PASSWORD = new char[strlen(PASSWORD) + 1];
    strcpy(this->PASSWORD, PASSWORD);

    return *this;
  }

  WebSocketHandler* build() {
    WebSocketHandler* instance = new WebSocketHandler(IP, PORT, SSID, PASSWORD);
    return instance;
  }

};

WebSocketsClient WebSocketHandler::webSocket;
Message WebSocketHandler::currentMessages[Global::NUMBER_OF_SLAVES];

#endif