<div align="center">

# 🚗 GestureCar

### ✋ Gesture-Controlled ESP32 Robotic Car

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![ESP32](https://img.shields.io/badge/ESP32-Bluetooth-green)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Gesture%20Recognition-orange)

Control a robotic car using only your hand gestures

</div>

---

GestureCar lets you control a robotic car using **vision-based gesture recognition**.
Your webcam detects gestures → Python interprets commands → Bluetooth sends signals → ESP32 drives the motors.

A fun blend of **Computer Vision + Robotics + Embedded Systems + Wireless Control**.

---

## ✨ Features

✅ Real-time gesture recognition
✅ Vision-based control (no physical remote)
✅ Wireless Bluetooth communication
✅ Smooth movement with low latency
✅ Beginner-friendly and low cost
✅ Voice feedback for actions using ElevenLabs AI voice generation

---

## 🧠 How It Works

```
Gesture → Camera → MediaPipe → Python Logic → Bluetooth → ESP32 → Motors → 🚗
```

1. Webcam captures your hand gestures
2. MediaPipe detects landmarks
3. Python recognizes the gesture
4. Command sent via Bluetooth
5. ESP32 drives the motors

---

## 🛠 Hardware Required

* ESP32 board
* L298N motor driver
* 2 DC motors
* Robot chassis + wheels
* Battery pack (I'm using a power bank)
* Jumper wires
* Webcam
* Laptop/PC with Bluetooth

---

## 💻 Software Required

### PC

* Python 3.9+
* OpenCV
* MediaPipe (Currently only works till version 0.10.21)
* PySerial
* Pygame

Install dependencies: (It's suggested that you do this in a virtual environment)

```bash
pip install opencv-python "mediapipe<=0.10.21" pyserial pygame

OR

pip install -r requirements.txt
```

### ESP32

* Arduino IDE
* ESP32 board package
* BluetoothSerial library

---

## 📂 Project Structure

```
GestureCar/
│
│── bt.py
│── gesture_car.py
│
├── car_control/
│   ├── car_control.ino
│
└── README.md
```

---

## 🎮 Gesture Controls

| Gesture      | Action        |
| ------------ | ------------- |
| ✊ Closed fist | Move forward  |
| ☝️ Index finger up    | Move backward |
| ✌️ Two fingers    | Turn left     |
| ✌️☝️ Three fingers   | Turn right    |
| ✋ Open palm  | Stop          |

Customize gestures inside `gestures.py`.

---

## 🚀 Setup

### 1️⃣ Upload ESP32 Code using Arduino IDE

```
car_control/car_control.ino
```

### 2️⃣ Pair Bluetooth

Pair ESP32 with your laptop and note the COM port

pls note: It's usually COM7 in that case don't change anything, if it's different go to the the bt.py and change the port to whatever it is.

### 3️⃣ Run Python

```
python gesture_car.py
```

### 4️⃣ Control the car

Show gestures to the camera and drive 🎉

---

## 🎯 Use Cases

* Touchless robotic control using vision
* Learning computer vision and embedded systems
* STEM and robotics school projects
* Gesture-based human–machine interaction demos
* Bluetooth automation experiments
* Prototyping smart rover systems
* Showcasing AI + robotics integration

---

## 🧩 Technologies Used

Python 🐍 • OpenCV 👁 • MediaPipe ✋ • Bluetooth 📡 • ESP32 🔌 • Embedded C++

---

## 👤 Author

**George Bijo**
