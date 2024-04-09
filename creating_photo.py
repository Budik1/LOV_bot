import pyautogui
from fun import  foto, see_tasks


def creating_photo_tasks():
    pos = see_tasks()
    width = 155
    height = 31
    x, y = pos
    x += 160
    y += 337
    r_x_1, r_y_1 = x, y
    foto("img/full_t/line_1.png", _region=(r_x_1, r_y_1, width, height))
    y += 91
    r_x_2, r_y_2 = x, y
    foto("img/full_t/line_2.png", _region=(r_x_2, r_y_2, width, height))
    y += 91
    r_x_3, r_y_3 = x, y
    foto("img/full_t/line_3.png", _region=(r_x_3, r_y_3, width, height))

def creating_photo_hero():
    in_hall_glory = pyautogui.locateCenterOnScreen('img/link_in_hall_glory.png', confidence=0.98)
    pyautogui.moveTo(in_hall_glory, duration=1)
    x, y = in_hall_glory
    y += 133
    x -= 225
    pos = x, y
    pyautogui.moveTo(pos, duration=1)
    foto('img/tests/test.png', (x, y, 140, 62))

def creating_photo_hero_ver():
    link_arena = pyautogui.locateCenterOnScreen('img/link_arena.png', confidence=0.98)
    pyautogui.moveTo(link_arena, duration=1)
    x, y = link_arena
    y += 20
    x += 15
    pos = x, y
    pyautogui.moveTo(pos, duration=1)
    foto('img/tests/test_ver.png', (x, y, 244, 493))


# creating_photo_tasks()
