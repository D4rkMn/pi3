#ifndef SLAVE_H
#define SLAVE_H

#include <WiFi.h>
#include <esp_now.h>
#include <esp_wifi.h>

#include "Message.h"
#include "Global.h"
#include "Addressable.h"

class Slave : public Addressable {
private:

  static Message currentMessage;
  static int LEDS[Global::NUMBER_OF_LEDS];

  static int32_t getWifiChannel(const char* SSID) {
    int32_t n = WiFi.scanNetworks();

    if (!n) {
      return 0;
    }

    for (uint8_t i = 0; i < n; i++) {
      if (!strcmp(SSID, WiFi.SSID(i).c_str())) {
        return WiFi.channel(i);
      }
    }
    return 0;
  }

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
    Serial.println("received");

    if (len != sizeof(Slave::currentMessage)) {
      Serial.println("Received data length mismatch");
      return;
    }

    Serial.println("data received ok");
    
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
    Slave::currentMessage.print();

    for (int i = 0; i < Global::NUMBER_OF_LEDS; i++) {
      digitalWrite(
        Slave::LEDS[i],
        Slave::currentMessage.getBit(i)
      );
    }
  }

  static void setupChannelBySSID(const char* SSID) {
    int32_t channel = Slave::getWifiChannel(SSID);
    WiFi.printDiag(Serial);
    esp_wifi_set_promiscuous(true);
    esp_wifi_set_channel(channel, WIFI_SECOND_CHAN_NONE);
    esp_wifi_set_promiscuous(false);
    WiFi.printDiag(Serial);
  }

};

Message Slave::currentMessage = Message();
int Slave::LEDS[Global::NUMBER_OF_LEDS];

#endif