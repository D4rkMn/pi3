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
Master master;

// I/O ports

const int LEFT = 4;
const int RIGHT = 19;


void setup() {

  delay(2000);

  Serial.begin(9600);

  WiFi.mode(WIFI_AP_STA);

  handler = WebSocketBuilder().
    setWiFi(SSID, PASSWORD).
    setHost(IP, PORT).
  build();

  delay(1000);

  //Slave::setupChannelBySSID(SSID);

  if (esp_now_init() != ESP_OK) {
    Serial.println("Error initializing ESPNOW");
    return;
  }

  
  /*
  Slave* slaveInstance = new Slave();
  // Message size = 1
  int LEDS[] = {5};
  slaveInstance->registerLEDS(LEDS);
  delay(1000);
  return;
  */
  

  uint8_t address[] = {0x34, 0x86, 0x5d, 0x3f, 0xb8, 0x70};
  Addressable *addressable = new Addressable(address);

  master.registerSlave(addressable);

  pinMode(LEFT, INPUT);
  pinMode(RIGHT, INPUT);

  delay(1000);

  Serial.println("start!");
}


void loop() {
  handler->loop();
  //return;

  // On right button press, send message to ESP32s
  bool array1[] = {(digitalRead(RIGHT) == HIGH)};
  Message message1(array1);
  Message messageArray[] = {message1};
  master.notifySlaves(messageArray);

  // On left button press, send message to WebSockets host
  if (digitalRead(LEFT) == HIGH) {
    const char* signal = "Hello server!";
    handler->sendSignal(signal);
  }

  delay(500);
}