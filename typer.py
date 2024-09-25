import pyautogui
import time

time.sleep(5)
with open('abc.txt','r')as f:
    lines = f.readlines()
    for line in lines:
        pyautogui.write(line.lstrip())