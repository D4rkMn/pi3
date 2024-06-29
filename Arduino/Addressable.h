#ifndef ADDRESSABLE_H
#define ADDRESSABLE_H

#include <WiFi.h>
#include <esp_wifi.h>

class Addressable {
protected:

  const uint8_t* macAddress;
  uint8_t tempAddress[6];

  // Automatically detects and sets mac address if its not already set
  bool obtainMacAddress() {
    uint8_t address[6];
    esp_err_t result = esp_wifi_get_mac(WIFI_IF_STA, tempAddress);

    if (result == ESP_OK) {
      macAddress = tempAddress;
      Serial.println("Success on MAC address");
      return true;
    }
    else {
      Serial.println("Failed to get MAC adddress");
      return false;
    }
  }

public:

  Addressable() {
    obtainMacAddress();
  }

  Addressable(const uint8_t* _macAddress) {
    for (int i = 0; i < 6; i++) {
      tempAddress[i] = _macAddress[i];
    }
    macAddress = tempAddress;
  }

  ~Addressable() {}

  const uint8_t* getMacAddress() const {
    return macAddress;
  }

  void printMacAddress() {
    Serial.printf("%02x:%02x:%02x:%02x:%02x:%02x\n",
      macAddress[0], macAddress[1], macAddress[2],
      macAddress[3], macAddress[4], macAddress[5]
    );
  }

};

#endif