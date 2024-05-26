import pyautogui
from time import sleep
import datetime
import baza_dannyx as b_d

log = 1

def my_print_to_file(text):
    if log == 1:
        date_time, date = time_now()
        file_name = date + ".txt"
        file = open(file_name, 'a+', encoding='utf-8')
        print(date_time, text, file=file)
        file.close()  # закрыть файл после работы с ним.


def time_now():
    now = datetime.datetime.now()
    # '%Y-%m-%d_%H:%M:%S' '%Y-%m-%d %H°%M\'\'%S\''
    date_time_now = (now.strftime('%Y-%m-%d %H:%M:%S'))
    date = (now.strftime('%Y-%m-%d'))
    return date_time_now, date


def move_to_click(pos_click: tuple, z_p_k: float):
    """
    Поместить указатель мыши по координатам и кликнуть, учитывая задержку.
    :param pos_click: Point
    :param z_p_k: задержка перед кликом(float)
    :return: None
    """

    my_print_to_file('move_to_click')
    sleep(0.3)
    pyautogui.moveTo(pos_click, duration=0.5, tween=pyautogui.easeInOutQuad)
    # print('должен быть клик')
    sleep(z_p_k)
    pyautogui.click(pos_click)
    sleep(0.18)


def push_close():
    it = 0
    my_print_to_file('fun.push_close')
    close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.89)
    while not close:
        it += 0.2
        sleep(0.1)
        close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.89)
        if it == int:
            my_print_to_file("поиск close")
    if close:
        my_print_to_file(f'close = {close}')
        move_to_click(close, 0.1)



def foto(path_name, _region):
    im1 = pyautogui.screenshot(region=_region)
    im1.save(path_name)


def find_link_i():
    inf = pyautogui.locateCenterOnScreen('img/info1.png', confidence=0.9)
    return inf


def see_tasks():
    """Открыть таверну"""
    taverna = pyautogui.locateCenterOnScreen('img/link_taverna.png', confidence=0.9)
    if taverna:
        pyautogui.moveTo(taverna, duration=1)
        return taverna
    else:
        pos = find_link_i()
        x, y = pos
        x += 70
        y += 140
        pos = x, y
        move_to_click(pos, 0.2)
        taverna = pyautogui.locateCenterOnScreen('img/link_taverna.png', confidence=0.9)
        while not taverna:
            sleep(0.1)
            taverna = pyautogui.locateCenterOnScreen('img/link_taverna.png', confidence=0.9)
        pyautogui.moveTo(taverna, duration=1)
        return taverna


def push_close_all_():
    # print('def "fun.push_close_all_"')
    close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.89)
    # print(close, 'close')
    while close:
        close_popup_window()
        push_close()
        sleep(1)
        close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.89)
        # print("цикл close")


def close_popup_window():
    print('def "fun.close_popup_window"')
    knob = pyautogui.locateCenterOnScreen('img/knob.png', confidence=0.89)
    cancel = pyautogui.locateCenterOnScreen('img/cancel.png', confidence=0.89)
    if knob:
        sleep(1)
        knob = pyautogui.locateCenterOnScreen('img/knob.png', confidence=0.89)
        move_to_click(knob, 1)
    if cancel:
        sleep(1)
        cancel = pyautogui.locateCenterOnScreen('img/cancel.png', confidence=0.89)
        print('нажал отменить')
        move_to_click(cancel, 1)


def exit_to_fountain():
    # print('fun.exit_to_fountain')
    to_fountain = pyautogui.locateCenterOnScreen('img/to_fountain_from_houses.png', confidence=0.9)
    while not to_fountain:
        sleep(1)
        print(to_fountain, 'to_fountain')
        to_fountain = pyautogui.locateCenterOnScreen('img/to_fountain_from_houses.png', confidence=0.85)

    move_to_click(to_fountain, 0.5)


def wait_close(txt):
    # print('fun.wait_close', txt)
    it = 0
    close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.89)
    while not close and it < 3:
        sleep(2)
        it += 1
        close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.89)
    # print('ждем close', it)
    sleep(0.2)
    close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.89)
    return close


def cancel_or_knob():
    it = 0
    cancel = pyautogui.locateCenterOnScreen('img/cancel.png', confidence=0.89)
    knob = pyautogui.locateCenterOnScreen('img/knob.png', confidence=0.89)
    while not cancel and not knob and it < 3:
        it += 0.2
        # print(cancel, '= cancel', knob, '= knob')
        sleep(0.1)
        cancel = pyautogui.locateCenterOnScreen('img/cancel.png', confidence=0.89)
        knob = pyautogui.locateCenterOnScreen('img/knob.png', confidence=0.89)
    if cancel:
        sleep(0.1)
        cancel = pyautogui.locateCenterOnScreen('img/cancel.png', confidence=0.89)
        move_to_click(cancel, 0)
    if knob:
        sleep(0.1)
        knob = pyautogui.locateCenterOnScreen('img/knob.png', confidence=0.89)
        move_to_click(knob, 0)
    close = wait_close('cancel_or_knob')
    return close


def selection_hero():
    gavril = pyautogui.locateCenterOnScreen('img/h_gavril.png', confidence=0.9)
    gadya = pyautogui.locateCenterOnScreen('img/h_gadya.png', confidence=0.9)
    veles = pyautogui.locateCenterOnScreen('img/h_veles.png', confidence=0.9)
    mara = pyautogui.locateCenterOnScreen('img/h_mara.png', confidence=0.9)
    if gavril:
        print('Гаврил')
        hero = 'Gavr'
        tasks = b_d.tasks_gold_g
    elif gadya:
        print('Гадя')
        hero = 'Gadya'
        tasks = b_d.tasks_gold_v
    elif veles:
        print('Велес')
        hero = 'Veles'
        tasks = b_d.tasks_gold_vel
    elif mara:
        print('Марьяна')
        hero = 'Mara'
        tasks = b_d.tasks_gold_mar
    else:
        print('не опознан')
        hero = None

    return hero


def to_fountain():
    fountain1 = pyautogui.locateCenterOnScreen('img/to_fountain_from_houses.png', confidence=0.9)
    fountain2 = pyautogui.locateCenterOnScreen('img/to_fountain_from_pier.png', confidence=0.9)
    if fountain1:
        print('от домов к фонтану')
        move_to_click(fountain1, 0)
    if fountain2:
        print('от пристани к фонтану')
        move_to_click(fountain2, 0)
    else:
        print('у фонтана')


def in_battle(par_conf, pos_i):
    my_print_to_file('in_battle')
    skip_battle = pyautogui.locateCenterOnScreen('img/skip_battle.png', confidence=par_conf)
    my_print_to_file(f'skip_battle = {skip_battle}')
    if skip_battle:
        x, y = pos_i
        y += 450
        pos_pet = x, y
        pyautogui.click(pos_pet)
        my_print_to_file('пропускаем бой')
        move_to_click(skip_battle, 0.2)

        return 1


def scroll_down():
    scroll_down_ = pyautogui.locateCenterOnScreen('img/scroll_down.png', confidence=0.98)
    while not scroll_down_:
        sleep(0.5)
        scroll_down_ = pyautogui.locateCenterOnScreen('img/scroll_down.png', confidence=0.98)
    sleep(0.1)
    return scroll_down_


def go_in_hall_glory():
    my_print_to_file('go_in_hall_glory')

    in_hall_glory = pyautogui.locateCenterOnScreen('img/link_in_hall_glory.png', confidence=0.98)
    hall_glory = pyautogui.locateCenterOnScreen('img/hall_glory.png', confidence=0.9999)
    close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.89)

    my_print_to_file(f'in_hall_glory = {in_hall_glory}')
    my_print_to_file(f'hall_glory = {hall_glory}')
    my_print_to_file(f'close = {close}')

    while not in_hall_glory:
        if close:
            push_close()
            sleep(1)
        elif hall_glory:
            my_print_to_file(f'hall_glory = {hall_glory}')
            move_to_click(hall_glory, 0.2)
            sleep(1)
        in_hall_glory = pyautogui.locateCenterOnScreen('img/link_in_hall_glory.png', confidence=0.98)
        hall_glory = pyautogui.locateCenterOnScreen('img/hall_glory.png', confidence=0.9999)
        close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.89)
