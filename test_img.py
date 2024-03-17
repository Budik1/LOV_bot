import pyautogui
from time import sleep
from fun import to_fountain
taverna = pyautogui.locateCenterOnScreen('img/taverna.png', confidence=0.9)
while taverna:
    print('taverna')
    sleep(1)
    taverna = pyautogui.locateCenterOnScreen('img/taverna.png', confidence=0.9)
print('No taverna')
# fountain1 = pyautogui.locateCenterOnScreen('img/to_fountain_from_houses.png', confidence=0.9)
# fountain2 = pyautogui.locateCenterOnScreen('img/to_fountain_from_pier.png', confidence=0.9)
#
# pyautogui.moveTo(fountain1)
# pyautogui.moveTo(fountain2)
# print(fountain1)
# print(fountain2)