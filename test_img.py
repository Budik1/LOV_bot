import pyautogui
from time import sleep

hall_glory = pyautogui.locateCenterOnScreen('img/hall_glory.png', confidence=0.9999)
print(hall_glory)