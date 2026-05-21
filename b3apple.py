import os
if os.name == 'nt':
   print("Running on Windows")
else: # posix (macos & linux)
   print("Running on a Unix-like OS")

import time
import os

def play_animation(frames, delay):
    clear_cmd = "cls" if os.name == "nt" else "clear" # cross platform
    
    
    MIN_DELAY = 0.01
    MAX_DELAY = 0.5

    if delay < MIN_DELAY:
        delay = MIN_DELAY
    elif delay > MAX_DELAY:
        delay = MIN_DELAY

    for frame in frames:
        if frame.strip() != "": # filter out blank frame
            os.system(clear_cmd)
            print(frame)
            time.sleep(delay)
try:
    # room on the broom
    with open("badapple.txt", "r", encoding="utf-8") as f:
        text = f.read()
        frames = text.split("nekomark")

        speed = float(input("Enter animation speed (e.g. 0.1): ")) -8 

        play_animation(frames, speed)

        print("Animation finished.")
except FileNotFoundError:
    print("file not found!")