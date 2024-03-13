import pyautogui
from time import sleep
from fun import see_tasks, move_to_click, cancel_or_knob, wait_close, push_close, find_link_i

par_conf = 0.9
conf = 0.99  # 0.962
tasks_v = {'t1': 'img/tasks/45x15.png', 't1-1': 'img/tasks/45x15_1.png',
           't2': 'img/tasks/90x30.png',
           't3': 'img/tasks/135x45.png',
           't4': 'img/tasks/180x60.png',
           't5': 'img/tasks/225x75.png',
           't6': 'img/tasks/270x90.png',
           }
tasks_g = {'t1_1': 'img/tasks_g/32x11_2.png', 't1_2': 'img/tasks_g/32x11_2.png',
           't2_1': 'img/tasks_g/63x21_1.png','t2_3': 'img/tasks_g/63x21_3.png',
           't3_2': 'img/tasks_g/95x32_2.png', 't3_3': 'img/tasks_g/95x32_3.png',
           't4_1': 'img/tasks_g/126x42_1.png', 't4_3': 'img/tasks_g/126x42_3.png',
           't5_2': 'img/tasks_g/158x53_2.png', 't5_3': 'img/tasks_g/158x53_3.png',
           }


def selection_hero():
    gavril = pyautogui.locateCenterOnScreen('img/gavril.png', confidence=0.9)
    gadya = pyautogui.locateCenterOnScreen('img/gadya.png', confidence=0.9)
    if gavril:
        print('Гаврил')
        tasks = tasks_g
    elif gadya:
        print('Гадя')
        tasks = tasks_v
    else:
        print('не опознан')
        tasks = None

    return tasks


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
                x, y = task_
                y -= 40
                click_task = x, y
                # move_to_click(task_, 2)
                pyautogui.moveTo(click_task)
                # variant_ = click_task
                return click_task
        conf -= 0.001
        print(f"поиск вариантов, conf ={conf}")





close = wait_close('проверка перса')
if close:
    move_to_click(close, 0)
tasks_ = selection_hero()

energy_ = 1
while energy_:
    see_tasks()
    variant = task_selection(tasks_)
    move_to_click(variant, 0.5)
    no_energy = verify_energy(4)
    if no_energy:
        print('NO ENERGY !!!')
        energy_ = None
        move_to_click(wait_close('NO ENERGY !!!'), 0.3)
    else:
        pos_i = find_link_i()
        print('Есть энергия')
        skip_battle = pyautogui.locateCenterOnScreen('img/skip_battle.png', confidence=par_conf)
        while not skip_battle:
            awake_friend = pyautogui.locateCenterOnScreen('img/awake_friend.png', confidence=par_conf)
            popup_xp = pyautogui.locateCenterOnScreen('img/popup_xp.png', confidence=par_conf)
            invite_friends = pyautogui.locateCenterOnScreen('img/invite_friends.png', confidence=par_conf)
            treasure = pyautogui.locateCenterOnScreen('img/treasure.png', confidence=par_conf)
            yes_go = pyautogui.locateCenterOnScreen('img/yes_go.png', confidence=par_conf)
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
            if skip_battle:
                # pyautogui.moveTo(pos_i)
                x, y = pos_i
                y += 450
                pos_pet = x, y
                pyautogui.click(pos_pet)
                move_to_click(skip_battle, 0.2)
                close = wait_close('skip_battle')
                if close:
                    print("1")
                    move_to_click(close, 0)
                sleep(2)
                # close = wait_close('skip_battle')
                # if close:
                #     print(2)
                #     move_to_click(close, 0)
                cansel_knob = cancel_or_knob()
                print()

