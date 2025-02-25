import pyautogui
import time
time.sleep(6)
with open('copy.txt','r')as f:
    lines=f.readlines()
    for line in lines:
        # print(line.lstrip())

        pyautogui.write(line.lstrip())
