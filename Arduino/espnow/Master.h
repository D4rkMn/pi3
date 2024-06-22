#ifndef MASTER_H
#define MASTER_H

#include <Vector.h>
#include <esp_now.h>
#include <WiFi.h>

#include "Addressable.h"
#include "Message.h"
#include "Global.h"

class Master {
private:

  Addressable* tempContainer[Global::MAX_SLAVES];
  Vector<Addressable*> slaves;
  esp_now_peer_info_t peerInfo = {};

public:

  Master() {
    slaves.setStorage(tempContainer);
  }

  ~Master() {}

  void registerSlave(Addressable* slave) {
    const uint8_t* macAddress = slave->getMacAddress();
    slave->printMacAddress();

    memcpy(peerInfo.peer_addr, macAddress, 6);
    peerInfo.channel = 0;
    peerInfo.encrypt = false;

    if (esp_now_add_peer(&peerInfo) != ESP_OK) {
      Serial.println("Failed to add peer!");
      return;
    }

    Serial.println("Registered peer correctly!");
    slaves.push_back(slave);
  }

  void notifySlaves(const Message& message) {
    for (auto slave : slaves) {
      notifySlave(slave, message);
    }
  }

  void notifySlave(Addressable* slave, const Message& message) {
    const uint8_t* macAddress = slave->getMacAddress();
    slave->printMacAddress();

    Serial.printf("message: %d\n", message.getBit(0));

    esp_err_t result = esp_now_send(macAddress, (uint8_t*) &message, sizeof(message));

    /*if (result == ESP_OK) {
      Serial.println("Sent with success");
    }
    else {
      Serial.println("Error sending data");
    }*/

    switch (result) {
      case ESP_OK:
        Serial.println("ok");
        break;
      case ESP_ERR_ESPNOW_NOT_INIT:
        Serial.println("not init");
        break;
      case ESP_ERR_ESPNOW_ARG:
        Serial.println("arg");
        break;
      case ESP_ERR_ESPNOW_INTERNAL:
        Serial.println("internal");
        break;
      case ESP_ERR_ESPNOW_NO_MEM:
        Serial.println("no mem");
        break;
      case ESP_ERR_ESPNOW_NOT_FOUND:
        Serial.println("not found");
        break;
      case ESP_ERR_ESPNOW_IF:
        Serial.println("if");
        break;
    }
  }

};

#endif