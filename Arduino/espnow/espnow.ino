#include "Master.h"
#include "Slave.h"
#include "Message.h"

#include <WiFi.h>

Master master;
Addressable* addressable = nullptr;

void setup() {

  Serial.begin(9600);
  WiFi.mode(WIFI_STA);

  if (esp_now_init() != ESP_OK) {
    Serial.println("Error initializing ESPNOW");
    return;
  }

  /*
  Slave slaveInstance;
  int LEDS[] = {5};
  currentInstance->registerLEDS(LEDS);
  */

  uint8_t address[] = {0x34, 0x86, 0x5d, 0x3f, 0xb8, 0x70};
  addressable = new Addressable(address);

  delay(1000);

  master.registerSlave(addressable);
}

// master: 34:86:5d:3a:eb:30
// slave: 34:86:5d:3f:b8:70

bool xd = true;

void loop() {
  bool array[] = {xd};
  xd = !xd;
  Message message(array);
  master.notifySlaves(message);
  delay(500);
}