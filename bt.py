import serial
import pygame


# ===========================================
# Serial + Audio Setup
# ===========================================

PORT = "COM7"
BAUD = 115200

bt = serial.Serial(PORT, BAUD, timeout=0.01)

pygame.mixer.init()

last_cmd = None

# ===========================================
# Sound helper
# ===========================================

def play(sound):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()


# play startup sound once when module loads
play('sounds/start.mp3')

# ===========================================
# Main function (called by gesture script)
# Sends command + handles sounds + listens ESP
# ===========================================

def command(cmd):
    global last_cmd

    # -------------------------
    # Always send command
    # -------------------------
    bt.write(cmd.encode())


    # -------------------------
    # Play sound only if changed
    # -------------------------
    if cmd != last_cmd:

        if cmd == 'F':
            play('sounds/forward.mp3')

        elif cmd == 'B':
            play('sounds/backward.mp3')

        elif cmd == 'L':
            play('sounds/left.mp3')

        elif cmd == 'R':
            play('sounds/right.mp3')

        print(f"Command sent: {cmd}")

        last_cmd = cmd

    # -------------------------
    # Read one message from ESP32
    # (non-blocking)
    # -------------------------
    if bt.in_waiting:
        line = bt.readline().decode(errors="ignore").strip()

        # ESP sends "D" when obstacle detected
        if line == "D":
            print("Obstacle detected!")