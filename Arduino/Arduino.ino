#include "Master.h"
#include "Slave.h"
#include "Message.h"
#include "WebSocketHandler.h"
#include "WiFiCredentials.h"
#include <WiFi.h>

// WiFi variables

const char* SSID = WIFI_SSID;
const char* PASSWORD = WIFI_PASSWORD;

const char* IP = HOST_IP;
const int PORT = HOST_PORT;

// Class object instances

WebSocketHandler* handler = nullptr;
Master* master = nullptr;

// I/O ports

const int LEFT = 4;
const int RIGHT = 19;


void setup() {

  delay(2000);

  Serial.begin(9600);
  WiFi.mode(WIFI_AP_STA);

  ///*
  handler = WebSocketBuilder().
    setWiFi(SSID, PASSWORD).
    setHost(IP, PORT).
  build();
  //*/

  delay(1000);

  /*
  Slave::setupChannelBySSID(SSID);
  */

  if (esp_now_init() != ESP_OK) {
    Serial.println("Error initializing ESPNOW");
    return;
  }

  /*
  Slave* slaveInstance = new Slave();
  // Message size = 1
  int LEDS[] = {
    // First char
    15, 4, 17, 18, 21, 22,
    // Second char
    13, 14, 26, 33, 32, 25
  };
  slaveInstance->printMacAddress();
  slaveInstance->registerLEDS(LEDS);
  delay(1000);
  return;
  */
  

  uint8_t address1[] = {0x34, 0x86, 0x5d, 0x3f, 0xb8, 0x70};
  Addressable* slave1 = new Addressable(address1);

  uint8_t address2[] = {0x34, 0x86, 0x5d, 0x3f, 0xe0, 0x7c};
  Addressable* slave2 = new Addressable(address2);

  uint8_t address3[] = {0xd4, 0x8a, 0xfc, 0xaa, 0x15, 0xcc};
  Addressable* slave3 = new Addressable(address3);

  master = new Master();
  master->registerSlave(slave1);
  master->registerSlave(slave2);
  master->registerSlave(slave3);

  pinMode(LEFT, INPUT);
  pinMode(RIGHT, INPUT);

  delay(1000);

  Serial.println("start!");
}


void loop() {
  //return;

  ///*
  handler->loop();
  const Message* messageArray = handler->getMessageArray();
  master->notifySlaves(messageArray);
  //*/

  // Handle button presses to iterate through the messages
  if (digitalRead(RIGHT) == HIGH) {
    const char* signal = "right";
    handler->sendSignal(signal);
  }
  else if (digitalRead(LEFT) == HIGH) {
    const char* signal = "left";
    handler->sendSignal(signal);
  }

  delay(500);
}