#include "BluetoothSerial.h"

BluetoothSerial SerialBT;

// -----------------------------
// Motor driver pins (L298N)
// -----------------------------
const int IN1_A = 14;
const int IN2_A = 27;
const int IN1_B = 26;
const int IN2_B = 25;

// -----------------------------
// Ultrasonic sensor pins
// -----------------------------
const int TRIG_PIN = 32;
const int ECHO_PIN = 33;

// -----------------------------
// Control variables
// -----------------------------
char cmd = 'S';                 // Current command (default Stop)
const float STOP_DISTANCE = 10.0; // Stop if object <= 10 cm


void setup() {

  // Motor pins as outputs
  pinMode(IN1_A, OUTPUT); 
  pinMode(IN2_A, OUTPUT);
  pinMode(IN1_B, OUTPUT); 
  pinMode(IN2_B, OUTPUT);

  // Ultrasonic pins
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  // Start Bluetooth with device name
  SerialBT.begin("Gesture Car");
}


void loop() {

  // -----------------------------
  // Read Bluetooth command (non-blocking)
  // -----------------------------
  if (SerialBT.available()) {
    cmd = SerialBT.read();
  }

  float distance = 1000; // default large value (safe)


  // =================================================
  // Only check distance when moving FORWARD
  // (saves time + avoids delay for other movements)
  // =================================================
  if (cmd == 'F') {

    // Trigger ultrasonic pulse
    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);

    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);

    digitalWrite(TRIG_PIN, LOW);

    // Measure echo time (timeout 25ms)
    long duration = pulseIn(ECHO_PIN, HIGH, 25000);

    // Convert time → distance (cm)
    distance = duration * 0.034 / 2.0;

    // If too close → stop and notify PC
    if (distance <= STOP_DISTANCE) {
      SerialBT.println("D");   // send "Obstacle detected"
      cmd = 'S';              // override command to Stop
    }
  }


  // =================================================
  // Motor control section
  // =================================================

  // Forward
  if (cmd == 'F') {
    digitalWrite(IN1_A,HIGH); digitalWrite(IN2_A,LOW);
    digitalWrite(IN1_B,HIGH); digitalWrite(IN2_B,LOW);
  } 

  // Backward
  else if (cmd == 'B') {
    digitalWrite(IN1_A,LOW); digitalWrite(IN2_A,HIGH);
    digitalWrite(IN1_B,LOW); digitalWrite(IN2_B,HIGH);
  } 

  // Left turn
  else if (cmd == 'L') {
    digitalWrite(IN1_A,HIGH); digitalWrite(IN2_A,LOW);
    digitalWrite(IN1_B,LOW);  digitalWrite(IN2_B,HIGH);
  } 

  // Right turn
  else if (cmd == 'R') {
    digitalWrite(IN1_A,LOW);  digitalWrite(IN2_A,HIGH);
    digitalWrite(IN1_B,HIGH); digitalWrite(IN2_B,LOW);
  } 

  // Stop (default)
  else {
    digitalWrite(IN1_A,LOW); digitalWrite(IN2_A,LOW);
    digitalWrite(IN1_B,LOW); digitalWrite(IN2_B,LOW);
  }
}
