from tkinter import *
import random

szinek = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Pink", "Brown", "Black", "White"]
ido_hatra = 45
pontszam = 0

def jatekKezdes(event):
    if ido_hatra == 45:
        szamlalas()
    kovetkezoSzin()

def kovetkezoSzin():
    global pontszam
    global ido_hatra
    if ido_hatra > 0:
        enter_beker.focus_set()
        if enter_beker.get().lower() == szinek[1].lower():
            pontszam += 2
        enter_beker.delete(0, END)
        random.shuffle(szinek)
        label.config(fg = str(szinek[1]), text = str(szinek[0]))
        pontszam_label.config(text = "Pontszám: " + str(pontszam))

def szamlalas():
    global ido_hatra
    if ido_hatra > 0:
        ido_hatra -= 1
        ido_label.config(text = "Idő hátra: " + str(ido_hatra))
        ido_label.after(1000, szamlalas)

szines_j_ablak = Tk()
szines_j_ablak.title("Színes játék")
szines_j_ablak.minsize(width = 600, height = 400)
szines_j_ablak.maxsize(width = 600, height = 400)

objektiv = Label(szines_j_ablak, text = "Írd be, hogy milyen színűek a betűk, és nem azt, amit kiír!")
objektiv.pack()
pontszam_label = Label(szines_j_ablak, text = "Írd be, hogy \"enter\" a játék kezdéséért!")
pontszam_label.pack()
ido_label = Label(szines_j_ablak, text = "Idő hátra: " + str(ido_hatra))
ido_label.pack()
label = Label(szines_j_ablak)
label.pack()
enter_beker = Entry(szines_j_ablak)
szines_j_ablak.bind('<Return>', jatekKezdes)
enter_beker.pack()
enter_beker.focus_set()

szines_j_ablak.mainloop()