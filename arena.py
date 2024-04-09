import pyautogui
from time import sleep, time
from fun import move_to_click, foto, push_close, find_link_i, in_battle, scroll_down, go_in_hall_glory

quantity_battles = 0
par_conf = 0.9


def battle_in_arena():
    global quantity_battles
    go_in_hall_glory()
    sleep(0.5)
    in_hall_glory = pyautogui.locateCenterOnScreen('img/link_in_hall_glory.png', confidence=0.98)
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

    attack = pyautogui.locateCenterOnScreen('img/attack.png', confidence=0.95, region=region_search)
    move_to_click(attack, 0.2)
    link_arena = pyautogui.locateCenterOnScreen('img/link_arena.png')
    while not link_arena:
        sleep(1)
        link_arena = pyautogui.locateCenterOnScreen('img/link_arena.png')
    hero_arena_ver = pyautogui.locateCenterOnScreen('img/hero_arena_ver.png')
    if hero_arena_ver:
        print('безоружен')
        quantity_battles += 1
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
    else:
        print('вооружён')


def inspection_hero():
    in_hall_glory = pyautogui.locateCenterOnScreen('img/link_in_hall_glory.png', confidence=0.98)
    x, y = in_hall_glory
    y += 170
    link = x, y

    return link


def search_unarmed():
    start_time = time()
    go_in_hall_glory()

    no_arms = pyautogui.locateCenterOnScreen('img/no_arm.png', confidence=0.98)
    while not no_arms:
        move_to_click(inspection_hero(), 0.05)

        ver_her_arms = pyautogui.locateCenterOnScreen('img/ver_her_arms.png', confidence=0.98)
        while not ver_her_arms:
            # sleep(0.2)
            ver_her_arms = pyautogui.locateCenterOnScreen('img/ver_her_arms.png', confidence=0.98)

        no_arms = pyautogui.locateCenterOnScreen('img/no_arm.png', confidence=0.98)
        if no_arms:
            print('no_arms')
        else:
            push_close()
            move_to_click(scroll_down(), 0.05)

    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, ' минут', seconds, ' сек.')

# search_unarmed()
