import pyautogui
from time import sleep
from fun import wait_close, foto, to_fountain, move_to_click, selection_hero, see_tasks

# close = wait_close('проверка')
# if close:
#     move_to_click(close, 0)
# to_fountain()
# tasks_ = selection_hero()

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

