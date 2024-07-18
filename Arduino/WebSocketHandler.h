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
        break;
      case WStype_TEXT:
        WebSocketHandler::parseResponse((char*)payload);
        break;
    }
  }

  // Given a response from the websockets host, it will be parsed and update the current message array
  static void parseResponse(char* response) {
    /*
      Format:
        111010
        010100
        011110
        001001
        000000
        000000
    */

    const int numRows = 6;
    const int numCols = 6;
    const int numConcatenatedLines = numRows / 2;
    char* concatenatedLines[numConcatenatedLines];

    // Create a modifiable copy of the input string
    char* str = new char[strlen(response) + 1];
    strcpy(str, response);

    // Tokenize the string using '\n' as the delimiter
    char* token = strtok(str, "\n");
    int i = 0;
    while (token != nullptr && i < numRows) {
      if (i % 2 == 0) {
        concatenatedLines[i / 2] = new char[numCols * 2 + 1];
        strcpy(concatenatedLines[i / 2], token);  // Copy the first line
      }
      else {
        strcat(concatenatedLines[i / 2], token);  // Concatenate the second line
      }
      token = strtok(nullptr, "\n");
      i++;
    }

    for (int i = 0; i < Global::NUMBER_OF_SLAVES; i++) {
      WebSocketHandler::currentMessages[i] = Message(concatenatedLines[i]);
      WebSocketHandler::currentMessages[i].print();
    }

    for (int i = 0; i < numConcatenatedLines; i++) {
      delete[] concatenatedLines[i];
    }
    delete[] str;
    
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