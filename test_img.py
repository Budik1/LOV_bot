import pyautogui
from time import sleep
from fun import next_haus, find_link_i, move_to_click
c = 0.
to_fountain = pyautogui.locateCenterOnScreen('img/to_fountain_1.png', confidence=0.95)  # 0.85
it = 0
# print(to_fountain)
while to_fountain:
    it += 1
    print(it)
    pyautogui.moveTo(to_fountain)
    sleep(1)
    pos_i = find_link_i()
    pyautogui.moveTo(pos_i, duration=1)
    next_haus()
    to_fountain = pyautogui.locateCenterOnScreen('img/to_fountain_1.png', confidence=0.95)  # 0.85

