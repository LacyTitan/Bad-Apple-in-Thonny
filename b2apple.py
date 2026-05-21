import time
import os

def play_animation(frames, delay):
    clear_cmd = "cls" if os.name == "nt" else "clear"

    for frame in frames:

        if frame.strip() != "":
            os.system(clear_cmd)
            print(frame)
            time.sleep(delay)
        else:
            pass

with open("badapple.txt", "r", encoding="utf-8") as f:
    text = f.read()


frames = text.split("nekomark")

speed = float(input("Enter animation speed (e.g. 0.1): "))

play_animation(frames, speed)

print("Animation finished.")