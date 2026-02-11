#include "BluetoothSerial.h"

BluetoothSerial SerialBT;

const int IN1_A = 14;
const int IN2_A = 27;
const int IN1_B = 26;
const int IN2_B = 25;

const int TRIG_PIN = 32;
const int ECHO_PIN = 33;

char cmd = 'S';
const float STOP_DISTANCE = 10.0;

void setup() {
  pinMode(IN1_A, OUTPUT); pinMode(IN2_A, OUTPUT);
  pinMode(IN1_B, OUTPUT); pinMode(IN2_B, OUTPUT);

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  SerialBT.begin("Gesture Car");
}

void loop() {
  if (SerialBT.available()) {
    cmd = SerialBT.read();
  }

  float distance = 1000; // default large value

  // Only check distance if moving forward
  if (cmd == 'F') {
    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);

    long duration = pulseIn(ECHO_PIN, HIGH, 25000);
    distance = duration * 0.034 / 2.0;

    if (distance <= STOP_DISTANCE) {
      SerialBT.println("D");
      cmd = 'S';  // override forward
    }
  }

  // Now handle motors for all commands
  if (cmd == 'F') {
    digitalWrite(IN1_A,HIGH); digitalWrite(IN2_A,LOW);
    digitalWrite(IN1_B,HIGH); digitalWrite(IN2_B,LOW);
  } 
  else if (cmd == 'B') {
    digitalWrite(IN1_A,LOW); digitalWrite(IN2_A,HIGH);
    digitalWrite(IN1_B,LOW); digitalWrite(IN2_B,HIGH);
  } 
  else if (cmd == 'L') {
    digitalWrite(IN1_A,HIGH); digitalWrite(IN2_A,LOW);
    digitalWrite(IN1_B,LOW); digitalWrite(IN2_B,HIGH);
  } 
  else if (cmd == 'R') {
    digitalWrite(IN1_A,LOW); digitalWrite(IN2_A,HIGH);
    digitalWrite(IN1_B,HIGH); digitalWrite(IN2_B,LOW);
  } 
  else {  // Stop
    digitalWrite(IN1_A,LOW); digitalWrite(IN2_A,LOW);
    digitalWrite(IN1_B,LOW); digitalWrite(IN2_B,LOW);
  }
}
