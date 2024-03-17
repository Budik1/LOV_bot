import pyautogui
from time import sleep
from fun import move_to_click, go_out_haus, find_link_i, find_sunduk, go_in_haus, next_haus, exit_to_fountain




def revision_of_house():
    sum_vi = 0
    find_su = 0
    link = find_link_i()
    x, y = link
    y += 570
    x += 40
    friend = x, y
    move_to_click(friend, 0.3)
    sleep(1)
    ik_haus = pyautogui.locateCenterOnScreen('img/ik_haus.png', confidence=0.9)
    move_to_click(ik_haus, 0.3)  # переход на экран домов
    while sum_vi < 15 and find_su < 10:
        go_in_haus()
        sum_vi += 1
        find_su += find_sunduk()
        print(sum_vi, "/", find_su)
        go_out_haus()
        if sum_vi < 14:
            next_haus()
    exit_to_fountain()
