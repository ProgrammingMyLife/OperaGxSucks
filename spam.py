import pyautogui as gui
import random
import time

urls = open("urls.txt", "r").read().splitlines()

while True:
    gui.moveTo(772,235,duration=0)
    gui.click()
    gui.write(random.choice(urls))   
    gui.press('enter') 
    time.sleep(3)

#x=772   y=235
