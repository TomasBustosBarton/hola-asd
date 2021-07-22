import pyautogui
import time


time.sleep(10)

for i in range(100):
    pyautogui.typewrite("a")
    pyautogui.press("enter")