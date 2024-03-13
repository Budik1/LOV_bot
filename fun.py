import pyautogui
from time import sleep


def move_to_click(pos_click: tuple, z_p_k: float):
    """
    Поместить указатель мыши по координатам и кликнуть, учитывая задержку.
    :param pos_click: Point
    :param z_p_k: задержка перед кликом(float)
    :return: None
    """
    # print('move_to_click', pos_click)
    sleep(0.3)
    pyautogui.moveTo(pos_click, duration=1, tween=pyautogui.easeInOutQuad)
    # print('должен быть клик')
    sleep(z_p_k)
    pyautogui.click(pos_click)
    sleep(0.18)


def push_close():
    # print('def "fun.push_close"')
    close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.89)
    if close:
        move_to_click(close, 0.1)


def foto(path_name, _region):
    im1 = pyautogui.screenshot(region=_region)
    im1.save(path_name)


def find_link_i():
    inf = pyautogui.locateCenterOnScreen('img/info1.png', confidence=0.9)
    return inf


def see_tasks():
    """Открыть таверну"""
    taverna = pyautogui.locateCenterOnScreen('img/taverna.png', confidence=0.9)
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
        taverna = pyautogui.locateCenterOnScreen('img/taverna.png', confidence=0.9)
        while not taverna:
            sleep(0.1)
            taverna = pyautogui.locateCenterOnScreen('img/taverna.png', confidence=0.9)
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
        move_to_click(knob, 1)
    if cancel:
        move_to_click(cancel, 1)


def find_sunduk():
    it = 0
    sunduk_1 = pyautogui.locateCenterOnScreen('img/sunduk_1.png', confidence=0.9)
    sunduk_2 = pyautogui.locateCenterOnScreen('img/sunduk_2.png', confidence=0.9)
    sunduk_3 = pyautogui.locateCenterOnScreen('img/sunduk_3.png', confidence=0.9)
    while not sunduk_1 and not sunduk_2 and it < 5:
        print(bool(sunduk_1), 'sunduk_1', bool(sunduk_2), 'sunduk_2', bool(sunduk_3), 'sunduk_3', it)
        sleep(0.3)
        it += 1
        sunduk_1 = pyautogui.locateCenterOnScreen('img/sunduk_1.png', confidence=0.9)
        sunduk_2 = pyautogui.locateCenterOnScreen('img/sunduk_2.png', confidence=0.9)
        sunduk_3 = pyautogui.locateCenterOnScreen('img/sunduk_3.png', confidence=0.9)
    if sunduk_1:
        move_to_click(sunduk_1, 0)
        close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)
        while not close:
            print('ждем close')
            sleep(0.1)
            close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)
        push_close()
        return 1
    elif sunduk_2:
        move_to_click(sunduk_2, 0)
        close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)
        while not close:
            print('ждем close')
            sleep(0.1)
            close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)
        push_close()
        return 1
    if sunduk_3:
        move_to_click(sunduk_3, 0)
        close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)
        while not close:
            print('ждем close')
            sleep(0.1)
            close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)
        push_close()
        return 1

    return 0


def go_in_haus():
    link = find_link_i()
    x, y = link
    x += 340
    y += 220
    haus = x, y
    move_to_click(haus, 0)
    to_fountain = pyautogui.locateCenterOnScreen('img/to_fountain.png', confidence=0.85)
    it = 0
    while to_fountain and it <= 10:
        it += 1
        to_fountain = pyautogui.locateCenterOnScreen('img/to_fountain.png', confidence=0.85)
    if to_fountain:
        return 0
    else:
        return 1


def go_out_haus():
    out_haus = pyautogui.locateCenterOnScreen('img/go_out_haus.png', confidence=0.9)
    while not out_haus:
        sleep(0.1)
        out_haus = pyautogui.locateCenterOnScreen('img/go_out_haus.png', confidence=0.9)
    move_to_click(out_haus, 0)


def next_haus():
    n_haus = pyautogui.locateCenterOnScreen('img/next_haus.png', confidence=0.8)
    while not n_haus:
        sleep(0.1)
        n_haus = pyautogui.locateCenterOnScreen('img/next_haus.png', confidence=0.8)
    move_to_click(n_haus, 0)


def exit_to_fountain():
    # print('fun.exit_to_fountain')
    to_fountain = pyautogui.locateCenterOnScreen('img/to_fountain.png', confidence=0.9)
    while not to_fountain:
        sleep(1)
        print(to_fountain, 'to_fountain')
        to_fountain = pyautogui.locateCenterOnScreen('img/to_fountain.png', confidence=0.85)

    move_to_click(to_fountain, 0.5)


def wait_close(txt):
    print('fun.wait_close', txt)
    it = 0
    close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.89)
    while not close and it < 3:
        sleep(2)
        it += 1
        close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.89)
    # print('ждем close', it)
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
