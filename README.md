GestureCar 🚗

GestureCar is an ESP32-based robotic car controlled using hand gestures.
A webcam captures your hand movements, Python processes them using MediaPipe,
and commands are sent wirelessly via Bluetooth to the ESP32 to drive the motors.

This project combines Computer Vision, Python programming, Bluetooth communication,
and embedded robotics.

FEATURES ✨

Real-time hand tracking

Wireless Bluetooth control

No physical remote required

Differential drive steering (no servo motor)

Smooth forward, backward, left, and right movement

Low latency response

Simple and low-cost hardware

HOW IT WORKS 🧠

Webcam captures your hand

MediaPipe detects hand landmarks

Python recognizes gestures

Commands sent through Bluetooth

ESP32 receives commands

Motor driver controls left and right motors

Flow:

Hand -> Camera -> Python -> Bluetooth -> ESP32 -> Motors -> Car moves

HARDWARE REQUIRED 🛠

ESP32 board

L298N or L293D motor driver

2 or 4 DC motors

Robot chassis with wheels

Battery pack

Jumper wires

Webcam

Laptop or PC with Bluetooth

Note: No servo motor is used. Turning is done by varying left/right motor speeds.

SOFTWARE REQUIRED 💻

PC Side:

Python 3.9 or newer

OpenCV

MediaPipe

PySerial

Install dependencies:

pip install opencv-python mediapipe pyserial

ESP32 Side:

Arduino IDE or PlatformIO

ESP32 board package

BluetoothSerial library

PROJECT STRUCTURE 📂

GestureCar/

python/
main.py - Camera + gesture detection + Bluetooth sender
gestures.py - Gesture recognition logic

esp32/
car_control.ino - Motor control code

README.txt

GESTURE CONTROLS 🎮

Hand forward -> Move forward
Hand back -> Move backward
Tilt left -> Turn left
Tilt right -> Turn right
Closed fist -> Stop

Gestures can be modified inside the Python code.

SETUP INSTRUCTIONS 🚀

Step 1:
Upload car_control.ino to ESP32 using Arduino IDE

Step 2:
Pair ESP32 with your laptop via Bluetooth

Step 3:
Run the program:

python main.py

Step 4:
Show gestures to the camera and control the car

CUSTOMIZATION IDEAS ⚙

Add speed control

Add more gestures

Add obstacle avoidance sensors

Use WiFi instead of Bluetooth

Use phone camera

Add video streaming

TECHNOLOGIES USED 🧩

Python
OpenCV
MediaPipe
Bluetooth
ESP32
Embedded C++

AUTHOR 👤

George Bijo
Robotics and Computer Vision Enthusiast
