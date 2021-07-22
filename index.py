import pyautogui
import time
import webbrowser
import winsound 
import random
from multiprocessing import Process

def virus():
    for i in range(10): 
        duration = 1000  # milliseconds
        freq = 880  # Hz
        winsound.Beep(freq, duration)
        time.sleep(1)

def virus1():
    url='https://www.youtube.com/watch?v=Nmcy8J6l8jE'
    for i in range(20):
        webbrowser.open_new(url)
        time.sleep(5)

def virus2():
    for i in range(50):
        pyautogui.typewrite("No apagues la compu")

def virus3():
    for i in range(10):
        pyautogui.alert('No apagues la compu')

def virus4():
    screenWidth, screenHeight = pyautogui.size()
    for i in range(500):
        pyautogui.moveTo(random.randint(0, screenWidth),random.randint(0, screenHeight))

if __name__ == '__main__':
  time.sleep(10)
  p1 = Process(target=virus)
  p1.start()
  p2 = Process(target=virus1)
  p2.start()
  p3=Process(target=virus3)
  p3.start()
  p4=Process(target=virus4)
  p4.start()
  p5=Process(target=virus2)
  p5.start()
  p1.join()
  p2.join()
  p3.join()
  p4.join()
  p5.join()