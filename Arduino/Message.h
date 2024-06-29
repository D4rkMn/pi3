#ifndef MESSAGE_H
#define MESSAGE_H

#include "Global.h"

class Message {
private:

    bool bits[Global::NUMBER_OF_LEDS];

public:

    Message() {
      for (int i = 0; i < Global::NUMBER_OF_LEDS; i++) {
        bits[i] = false;
      }
    }

    Message(const bool* _bits) : bits(_bits) {
      for (int i = 0; i < Global::NUMBER_OF_LEDS; i++) {
        bits[i] = _bits[i];
      }
    }

    bool getBit(int n) const {
      return bits[n];
    }

    void print() const {
      char result[Global::NUMBER_OF_LEDS+1];
      for (int i = 0; i < Global::NUMBER_OF_LEDS; i++) {
        result[i] = bits[i] ? '1' : '0';
      }
      result[Global::NUMBER_OF_LEDS] = '\0';
      Serial.printf("message: %s\n", result);
    }

};

#endif