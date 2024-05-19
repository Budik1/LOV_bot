import pyautogui
from time import sleep
from fun import move_to_click, find_link_i, push_close, exit_to_fountain, selection_hero
from PIL import ImageTk


def next_haus():
    n_haus = pyautogui.locateCenterOnScreen('img/next_haus.png', confidence=0.8)
    while not n_haus:
        sleep(0.1)
        n_haus = pyautogui.locateCenterOnScreen('img/next_haus.png', confidence=0.8)
    move_to_click(n_haus, 0)


def go_in_haus():
    link = find_link_i()
    x, y = link
    x += 340
    y += 220
    haus = x, y
    to_fountain = pyautogui.locateCenterOnScreen('img/to_fountain_from_houses.png', confidence=0.85)
    while not to_fountain:
        sleep(0.25)
        to_fountain = pyautogui.locateCenterOnScreen('img/to_fountain_from_houses.png', confidence=0.85)
        if to_fountain:
            print(to_fountain, 'to_fountain v go_in_haus')
    sleep(0.5)
    path_haus = pyautogui.locateCenterOnScreen('img/path_haus.png', confidence=0.9)
    print(path_haus, 'path_haus до')
    it = 0
    while not path_haus and it < 3:
        print('поиск дорожки к дому')
        sleep(0.2)
        it += 0.5
        path_haus = pyautogui.locateCenterOnScreen('img/path_haus.png', confidence=0.9)
    if path_haus:
        print(path_haus, 'path_haus')
        while path_haus:
            move_to_click(haus, 0)
            sleep(0.5)
            path_haus = pyautogui.locateCenterOnScreen('img/path_haus.png', confidence=0.9)
        out_haus = pyautogui.locateCenterOnScreen('img/go_out_haus.png', confidence=0.9)
        while not out_haus:
            sleep(0.1)
            out_haus = pyautogui.locateCenterOnScreen('img/go_out_haus.png', confidence=0.9)
        return 1
    else:
        pyautogui.move(50, 50)
        return 0


def to_house():
    ik_haus = pyautogui.locateCenterOnScreen('img/ik_haus.png', confidence=0.9)
    while not ik_haus:
        sleep(0.5)
        ik_haus = pyautogui.locateCenterOnScreen('img/ik_haus.png', confidence=0.9)

    return ik_haus


def find_sunduk():
    it = 0
    sunduk_1 = pyautogui.locateCenterOnScreen('img/sunduk_1.png', confidence=0.9)
    sunduk_2 = pyautogui.locateCenterOnScreen('img/sunduk_2.png', confidence=0.9)
    sunduk_3 = pyautogui.locateCenterOnScreen('img/sunduk_3.png', confidence=0.9)
    while not sunduk_1 and not sunduk_2 and not sunduk_3 and it < 5:
        print(bool(sunduk_1), 'sunduk_1', bool(sunduk_2), 'sunduk_2', bool(sunduk_3), 'sunduk_3', it)
        sleep(1)
        it += 1
        sunduk_1 = pyautogui.locateCenterOnScreen('img/sunduk_1.png', confidence=0.9)
        sunduk_2 = pyautogui.locateCenterOnScreen('img/sunduk_2.png', confidence=0.9)
        sunduk_3 = pyautogui.locateCenterOnScreen('img/sunduk_3.png', confidence=0.9)
    if sunduk_1:
        return sunduk_1
    elif sunduk_2:
        return sunduk_2
    if sunduk_3:
        return sunduk_3
    else:
        return None


def go_out_haus():
    out_haus = pyautogui.locateCenterOnScreen('img/go_out_haus.png', confidence=0.9)
    while not out_haus:
        sleep(0.1)
        out_haus = pyautogui.locateCenterOnScreen('img/go_out_haus.png', confidence=0.9)
    move_to_click(out_haus, 0)


def revision_of_house():
    hero = selection_hero()
    sum_vi = 0
    find_su = 0
    link = find_link_i()
    x, y = link
    y += 570
    x += 40
    friend = x, y
    move_to_click(friend, 0.3)
    sleep(1)
    ik_haus = to_house()
    move_to_click(ik_haus, 0.3)  # переход на экран домов
    while find_su < 10:  # sum_vi < 15 and
        vizit = go_in_haus()
        if vizit:
            sum_vi += 1
            sunduk = find_sunduk()
            if sunduk:
                move_to_click(sunduk, 0.2)
                find_su += 1
                close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.89)
                while not close:
                    sleep(0.2)
                    close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.89)
                    if close:
                        move_to_click(close, 0.2)
            print(sum_vi, "/", find_su)

            go_out_haus()
            if sum_vi < 14:
                next_haus()
        else:
            sum_vi += 1
            print(sum_vi, "/", find_su)
            next_haus()
    exit_to_fountain()
