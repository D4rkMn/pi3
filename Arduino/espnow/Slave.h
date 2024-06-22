#ifndef SLAVE_H
#define SLAVE_H

#include <WiFi.h>
#include <esp_wifi.h>

#include "Message.h"
#include "Global.h"
#include "Addressable.h"

class Slave : public Addressable {
private:

  static Message currentMessage;
  static int LEDS[Global::NUMBER_OF_LEDS];

public:

  Slave() {
    if (obtainMacAddress()) {
      esp_now_register_recv_cb(Slave::onDataReceive);
    }
  }

  Slave(const uint8_t* macAddress) {
    this->macAddress = macAddress;
    esp_now_register_recv_cb(Slave::onDataReceive);
  }

  ~Slave() {}

  static void onDataReceive(const esp_now_recv_info* mac, const uint8_t* incomingData, int len) {
    if (len != sizeof(Slave::currentMessage)) {
      Serial.println("Received data length mismatch");
      return;
    }
    
    memcpy(&Slave::currentMessage, incomingData, sizeof(Slave::currentMessage));
    Slave::processMessage();
  }

  void registerLEDS(const int* _LEDS) {
    for (int i = 0; i < Global::NUMBER_OF_LEDS; i++) {
      Slave::LEDS[i] = _LEDS[i];
      pinMode(_LEDS[i], OUTPUT);
    }
  }

  static void processMessage() {
    for (int i = 0; i < Global::NUMBER_OF_LEDS; i++) {
      digitalWrite(
        Slave::LEDS[i],
        Slave::currentMessage.getBit(i)
      );
    }
  }

};

Message Slave::currentMessage = Message();
int Slave::LEDS[Global::NUMBER_OF_LEDS];

#endif