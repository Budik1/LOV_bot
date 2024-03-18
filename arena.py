import pyautogui
from time import sleep
from fun import move_to_click, foto, push_close, find_link_i, in_battle

par_conf = 0.9

def battle_in_arena():
    hall_glory = pyautogui.locateCenterOnScreen('img/hall_glory.png', confidence=0.9999)
    # print(hall_glory, 'hall_glory')
    if not hall_glory:
        push_close()
        sleep(1)
    hall_glory = pyautogui.locateCenterOnScreen('img/hall_glory.png', confidence=0.9999)
    move_to_click(hall_glory, 0.2)
    in_hall_glory = pyautogui.locateCenterOnScreen('img/linck_in_hall_glory.png', confidence=0.98)
    while not in_hall_glory:
        sleep(1)
        in_hall_glory = pyautogui.locateCenterOnScreen('img/linck_in_hall_glory.png', confidence=0.98)
    sleep(0.5)
    in_hall_glory = pyautogui.locateCenterOnScreen('img/linck_in_hall_glory.png', confidence=0.98)
    x, y = in_hall_glory
    x -= 300
    y += 100
    region_search = x, y, 650, 120
    hero_arena = pyautogui.locateCenterOnScreen('img/hero_arena.png', confidence=0.98, region=region_search)
    # print(hero_arena, 'hero_arena')
    while not hero_arena:
        scroll_down = pyautogui.locateCenterOnScreen('img/scroll_down.png', confidence=0.98)
        while not scroll_down:
            sleep(0.5)
            scroll_down = pyautogui.locateCenterOnScreen('img/scroll_down.png', confidence=0.98)
            print(scroll_down, 'scroll_down в цикле поиска')
        scroll_down = pyautogui.locateCenterOnScreen('img/scroll_down.png', confidence=0.98)
        # print(scroll_down, 'scroll_down нажимаем')
        move_to_click(scroll_down, 0.2)
        sleep(1)
        hero_arena = pyautogui.locateCenterOnScreen('img/hero_arena.png', confidence=0.98, region=region_search)

    # hero_arena = pyautogui.locateCenterOnScreen('img/hero_arena.png', confidence=0.98, region=region_search)
    # pyautogui.moveTo(hero_arena, duration=2)
    attack = pyautogui.locateCenterOnScreen('img/attack.png', confidence=0.95, region=region_search)
    move_to_click(attack, 0.2)
    linck_arena = pyautogui.locateCenterOnScreen('img/linck_arena.png')
    while not linck_arena:
        sleep(1)
        linck_arena = pyautogui.locateCenterOnScreen('img/linck_arena.png')
    hero_arena_ver = pyautogui.locateCenterOnScreen('img/hero_arena_ver.png')
    if hero_arena_ver:
        print('безоружен')

    pos_i = find_link_i()
    in_battl = pyautogui.locateCenterOnScreen('img/in_battle.png')
    while not in_battl:
        sleep(1)
        in_battl = pyautogui.locateCenterOnScreen('img/in_battle.png')
    move_to_click(in_battl, 0.2)
    # print(pos_i)
    skip_battle = pyautogui.locateCenterOnScreen('img/skip_battle.png', confidence=par_conf)
    while not skip_battle:
        sleep(1)
        skip_battle = pyautogui.locateCenterOnScreen('img/skip_battle.png', confidence=par_conf)
    # print("есть пропустить бой")
    in_battle(par_conf, pos_i)
    close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.89)
    while not close:
        sleep(0.2)
        close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.89)
    sleep(0.2)
    close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.89)
    move_to_click(close, 0.1)
    sleep(1)



