import pyautogui
from time import sleep

path_haus = pyautogui.locateCenterOnScreen('img/path_haus.png', confidence=0.9)
print(path_haus)