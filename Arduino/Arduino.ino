// Define the port used for serial comunication
const int SERIAL_PORT = 9600;

// Define the I/O ports
const int LED = 2;
const int BUTTON = 18;

// Variable to save the last value of the LED output
uint8_t lastValue = LOW;

void setup() {
  Serial.begin(SERIAL_PORT);
  pinMode(LED, OUTPUT);
  pinMode(BUTTON, INPUT);
}

void loop() {
  // Await button press. Meanwhile, hold last output value
  while (digitalRead(BUTTON) != HIGH) {
    digitalWrite(LED, lastValue);
  }
  delay(500);
  Serial.println("next");

  // If Python isn't sending serial, then do nothing
  if (Serial.available() <= 0) {
    return;
  }

  // Read from Python, then output
  char option = Serial.read();

  if (option == '0') {
    digitalWrite(LED, LOW);
    lastValue = LOW;
  }
  if (option == '1') {
    digitalWrite(LED, HIGH);
    lastValue = HIGH;
  }

}