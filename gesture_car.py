import cv2                      # OpenCV for camera + image processing
import mediapipe as mp          # MediaPipe for hand tracking
import bt                       # Your Bluetooth module (ESP32 control)

# -------------------------------
# 🎨 Drawing color settings (BGR)
# -------------------------------
LANDMARK_COLOR = (0, 255, 0)      # finger dots
CONNECTION_COLOR = (0, 200, 0)    # finger lines
BOX_COLOR = (255, 98, 0)          # bounding box
TEXT_COLOR = (255, 98, 0)         # gesture text


# -------------------------------
# MediaPipe setup
# -------------------------------
mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils

# Initialize hand detection
hands = mpHands.Hands(
    static_image_mode=False,    # Video stream (not images)
    max_num_hands=1,            # Detect only one hand
    model_complexity=1,         # Balance between speed & accuracy
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Landmark IDs for finger tips
tipIds = [4, 8, 12, 16, 20]

# -------------------------------
# Camera setup
# -------------------------------
cap = cv2.VideoCapture(0)       # Use external camera (change if needed)
cv2.namedWindow("GestureCar", cv2.WINDOW_NORMAL)

# -------------------------------
# Main loop
# -------------------------------
while True:
    success, img = cap.read()   # Read camera frame
    if not success:
        break

    h, w, c = img.shape         # Image dimensions

    # Convert BGR → RGB for MediaPipe
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    # -------------------------------
    # If hand detected
    # -------------------------------
    if results.multi_hand_landmarks:
        for handLms, handInfo in zip(
                results.multi_hand_landmarks,
                results.multi_handedness):

            lmList = []         # Stores landmark coordinates
            xList = []          # All x values
            yList = []          # All y values

            # Extract landmarks
            for id, lm in enumerate(handLms.landmark):
                px, py, pz = int(lm.x * w), int(lm.y * h), int(lm.z * w)
                lmList.append([px, py, pz])
                xList.append(px)
                yList.append(py)

            # Bounding box around hand
            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)
            bbox = xmin, ymin, xmax - xmin, ymax - ymin
            cx = bbox[0] + bbox[2] // 2
            cy = bbox[1] + bbox[3] // 2

            # Detect hand type (left / right)
            handType = handInfo.classification[0].label

            # Flip because webcam is mirrored
            if handType == "Right":
                handType = "Left"
            else:
                handType = "Right"

            fingers = []        # Stores open(1)/closed(0) state

            # -------------------------------
            # Thumb logic (depends on hand side)
            # -------------------------------
            if handType == "Right":
                fingers.append(1 if lmList[tipIds[0]][0] >
                                   lmList[tipIds[0] - 1][0] else 0)
            else:
                fingers.append(1 if lmList[tipIds[0]][0] <
                                   lmList[tipIds[0] - 1][0] else 0)

            # -------------------------------
            # Other 4 fingers (y-axis check)
            # -------------------------------
            for id in range(1, 5):
                fingers.append(1 if lmList[tipIds[id]][1] <
                                   lmList[tipIds[id] - 2][1] else 0)

            # -------------------------------
            # Gesture mapping
            # -------------------------------
            if fingers == [0, 0, 0, 0, 0] or fingers == [1, 0, 0, 0, 0]:
                gesture = "F"   # Forward
            elif fingers == [1, 1, 1, 1, 1]:
                gesture = "S"   # Stop
            elif fingers == [0, 1, 0, 0, 0]:
                gesture = "B"   # Backward
            elif fingers == [0, 1, 1, 0, 0]:
                gesture = "L"   # Left
            elif fingers == [0, 1, 1, 1, 0]:
                gesture = "R"   # Right
            else:
                gesture = "S"   # Default stop

            # Send command to ESP32
            bt.command(gesture)

            # Draw hand landmarks (custom colors added)
            mpDraw.draw_landmarks(
                img,
                handLms,
                mpHands.HAND_CONNECTIONS,
                mpDraw.DrawingSpec(color=LANDMARK_COLOR, thickness=3, circle_radius=4),
                mpDraw.DrawingSpec(color=CONNECTION_COLOR, thickness=2)
            )

            # Draw bounding box
            cv2.rectangle(
                img,
                (bbox[0] - 20, bbox[1] - 20),
                (bbox[0] + bbox[2] + 20, bbox[1] + bbox[3] + 20),
                BOX_COLOR,
                2
            )

            # Display gesture text
            cv2.putText(
                img,
                gesture,
                (bbox[0] - 30, bbox[1] - 30),
                cv2.FONT_HERSHEY_PLAIN,
                2,
                TEXT_COLOR,
                2
            )

    # -------------------------------
    # No hand → Stop car
    # -------------------------------
    else:
        bt.command('S')

    # Show camera feed
    cv2.imshow("GestureCar", img)

    # Quit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        bt.command('S')
        break

# -------------------------------
# Cleanup
# -------------------------------
cap.release()

cv2.destroyAllWindows()

