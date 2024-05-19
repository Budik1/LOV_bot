from tkinter import *
from tkinter import ttk
# from PIL import ImageTk
# import fun
import revision_of_house as r_h
import energy
import arena


def arena_battl():
    attempts = 0
    while True:
        arena.battle_in_arena()
        attempts += 1
        print(f'попытка {attempts}, Бой {arena.quantity_battles}')


root = Tk()

root.title('помощник "L_O_V"')
root.geometry("388x130+1195+50")  # Ширина x Высота + координата X + координата Y
root.resizable(False, False)

gadya_case = StringVar(value='0')
gavr_case = StringVar(value='0')

ttk.Button(text="сбор сундуков", width=13, command=r_h.revision_of_house).place(x=0, y=0)
ttk.Button(text="энергия в золото", width=16, command=energy.energy_gold).place(x=0, y=30)
ttk.Button(text="энергия в опыт", width=16, command=energy.energy_xp).place(x=170, y=30)
ttk.Button(text="арена", width=13, command=arena_battl).place(x=0, y=60)
ttk.Label(text="V/").place(x=140, y=0)
ttk.Label(textvariable=gadya_case).place(x=160, y=0)
ttk.Label(text="G/").place(x=190, y=0)
ttk.Label(textvariable=gavr_case).place(x=210, y=0)
# ttk.Button(text=" сбор бонуса ", width=13, command=fun.bonus, state="disabled").place(x=0, y=32)
# ttk.Label(text=status_bonus).place(x=130, y=32)
# ttk.Button(text="  сбор подарков  ", width=13, command=fun.station_gifts, state="disabled").place(x=0, y=64)
# ttk.Button(text=" обход VIP ", width=13, command=tent_inspection).place(x=0, y=96)
# ttk.Label(textvariable=status_vip).place(x=130, y=96)
# # шаг 31
# ttk.Button(text=" на Киевскую ", width=11, command=touring.frunze_kiev).place(x=120, y=169)
# ttk.Button(text=" домой ", width=11, command=touring.kiev_frunze).place(x=120, y=200)
# ttk.Button(text="кикиморы", width=11, command=touring.za_kikimorami).place(x=153, y=31)
# ttk.Label(textvariable=status_kiki, background="#FFCDD2", foreground="#B71C1C", padding=4).place(x=263, y=31)
# ttk.Button(text="Паук + Ящер", width=11, command=touring.pauk_yascher).place(x=153, y=0)
#
# ttk.Button(text="test гардероб", width=11, command=person.pereodevanie).place(x=109, y=245)
#
# ttk.Button(text="most_frunze", width=11, command=touring.most_frunze).place(x=218, y=277)
# ttk.Button(text="frunze_most", width=11, command=touring.frunze_most).place(x=218, y=308)
#
# ttk.Button(text="most_riga", width=11, command=touring.most_riga).place(x=109, y=277)  # x=133
# ttk.Button(text="riga_most", width=11, command=touring.riga_most).place(x=109, y=308)
#
# ttk.Button(text="frunze_riga", width=11, command=touring.frunze_riga).place(x=0, y=277)
# ttk.Button(text="riga_frunze", width=11, command=touring.riga_frunze).place(x=0, y=308)
#

# imagePul = ImageTk.PhotoImage(file="img/pulya.png")
# ttk.Button(root, image=imagePul, command=station_master.vybor_zadaniya_na_puli).place(x=60, y=145)
#
# img_e1 = ImageTk.PhotoImage(file="img/en1v3.png")
# ttk.Button(root, image=img_e1, command=en_1).place(x=0, y=128)
# #
# img_e2 = ImageTk.PhotoImage(file="img/en2v3.png")
# ttk.Button(root, image=img_e2, command=en_2).place(x=0, y=168)
# #
# img_e3 = ImageTk.PhotoImage(file="img/en3v3.png")
# ttk.Button(root, image=img_e3, command=en_3).place(x=0, y=208)

root.mainloop()
