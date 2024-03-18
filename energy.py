import pyautogui
from time import sleep
from fun import see_tasks, move_to_click, cancel_or_knob, wait_close, find_link_i, selection_hero, foto, in_battle

par_conf = 0.9
conf = 0.99  # 0.962





def verify_energy(q_it):
    it = 0
    not_energy = pyautogui.locateCenterOnScreen('img/not_energy.png', confidence=0.9)
    while not not_energy and it < q_it:
        # print(not_energy, 'not_energy', it)
        it += 1
        sleep(1)
        not_energy = pyautogui.locateCenterOnScreen('img/not_energy.png', confidence=0.9)
    return not_energy


def task_selection(tasks):
    variant_ = None
    conf = 0.99
    while not variant_:
        for img in tasks:
            task_ = pyautogui.locateCenterOnScreen(tasks[img], confidence=conf)
            if task_:
                print(f"{tasks[img]}, conf={conf}")
                print('проверь наличие и место')
                x, y = task_
                y -= 40
                click_task = x, y
                # move_to_click(task_, 2)
                pyautogui.moveTo(click_task)
                # variant_ = click_task
                return click_task
        conf -= 0.001
        print(f"поиск вариантов, conf ={conf}")


def energy():
    close = wait_close('проверка перса')
    if close:
        move_to_click(close, 0)
    tasks_ = selection_hero()

    energy_ = 1
    it_f =1
    while energy_:
        see_tasks()
        variant = task_selection(tasks_)
        # pyautogui.moveTo(variant)  # отладка
        move_to_click(variant, 0.5)  # автомат
        no_energy = verify_energy(4)
        if no_energy:
            print('NO ENERGY !!!')
            energy_ = None
            move_to_click(wait_close('NO ENERGY !!!'), 0.3)
        else:
            pos_i = find_link_i()
            print('Есть энергия')
            taverna = pyautogui.locateCenterOnScreen('img/linck_taverna.png', confidence=0.9)
            while taverna:
                sleep(1)
                taverna = pyautogui.locateCenterOnScreen('img/linck_taverna.png', confidence=0.9)

            skip_battle = pyautogui.locateCenterOnScreen('img/skip_battle.png', confidence=par_conf)
            while not skip_battle:
                awake_friend = pyautogui.locateCenterOnScreen('img/_awake_friend.png', confidence=par_conf)
                popup_xp = pyautogui.locateCenterOnScreen('img/_popup_xp.png', confidence=par_conf)
                invite_friends = pyautogui.locateCenterOnScreen('img/_invite_friends.png', confidence=par_conf)
                treasure = pyautogui.locateCenterOnScreen('img/_treasure.png', confidence=par_conf)
                yes_go = pyautogui.locateCenterOnScreen('img/_yes_go.png', confidence=par_conf)
                if popup_xp:
                    print('я учту это')
                    move_to_click(popup_xp, 0.1)
                    move_to_click(wait_close('я учту это'), 0)
                if invite_friends:
                    print('Пригласить друга')
                    move_to_click(invite_friends, 0.1)
                    move_to_click(cancel_or_knob(), 0)
                    # cancel_or_knob()
                    # push_close()
                    close = wait_close('Пригласить друга')
                    if close:
                        move_to_click(close, 0)
                if treasure:
                    print('Искать клад')
                    move_to_click(treasure, 0.1)
                    move_to_click(cancel_or_knob(), 0)
                    # cancel_or_knob()
                    # push_close()
                if yes_go:
                    print('Да, поехали')
                    move_to_click(yes_go, 0.1)
                if awake_friend:
                    print('Разбудить друга')
                    move_to_click(awake_friend, 0.1)
                    # cancel_or_knob()
                    # push_close()
                    move_to_click(cancel_or_knob(), 0)
                    close = wait_close('Разбудить друга')
                    if close:
                        move_to_click(close, 0)
                skip_battle = pyautogui.locateCenterOnScreen('img/skip_battle.png', confidence=par_conf)
                end = in_battle(par_conf, pos_i)
                if end:
                    close = wait_close('skip_battle')
                    if close:
                        move_to_click(close, 0)
                    sleep(2)
                    cansel_knob = cancel_or_knob()
                    if cansel_knob:
                        close = wait_close('skip_battle')
                        if close:
                            move_to_click(close, 0)
                    print()
                    # energy_ = 0
