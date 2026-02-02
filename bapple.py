import time
import os

# 设定每帧延迟（秒），可自行调整速度
FRAME_DELAY = 0.1

# 读取 badapple.txt
with open("badapple.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 分割成多个画面，以 "nekomark" 为分隔
frames = [frame.strip() for frame in text.split("nekomark") if frame.strip()]

# 自动侦测系统清屏指令
clear_cmd = "cls" if os.name == "nt" else "clear"

# 播放
try:
    while True:
        for frame in frames:
            os.system(clear_cmd)
            print(frame)
            time.sleep(FRAME_DELAY)
except KeyboardInterrupt:
    print("\n動畫已停止。")
