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
    global pontszam
    if ido_hatra > 0:
        ido_hatra -= 1
        ido_label.config(text = "Idő hátra: " + str(ido_hatra))
        ido_label.after(1000, szamlalas)
    if ido_hatra == 0:
        if pontszam == 0:
            szines_j_win = Toplevel()
            objektiv = Label(szines_j_win, text = "Add fel", font = ('Helvetica', 15))
            objektiv.pack()
        elif pontszam > 1 and pontszam <= 10:
            szines_j_win = Toplevel()
            objektiv = Label(szines_j_win, text = "Ne add fel! Menni fog!", font = ('Helvetica', 15))
            objektiv.pack()
        elif pontszam > 11 and pontszam <= 20:
            szines_j_win = Toplevel()
            objektiv = Label(szines_j_win, text = "Már majdnem jónak számítasz!", font = ('Helvetica', 15))
            objektiv.pack()
        elif pontszam > 21 and pontszam <= 30:
            szines_j_win = Toplevel()
            objektiv = Label(szines_j_win, text = "Egész jó!", font = ('Helvetica', 15))
            objektiv.pack()
        elif pontszam > 30:
            for i in range (15):
                szines_j_win = Toplevel()
                objektiv = Label(szines_j_win, text = "VEDD MEG A SPART!!!!!", font = ('Helvetica', 15))
                objektiv.pack()
                szines_j_win = Toplevel()
                objektiv = Label(szines_j_win, text = "VEDD MEG A SPART!!!!!", font = ('Helvetica', 15))
                objektiv.pack()
                szines_j_win = Toplevel()
                objektiv = Label(szines_j_win, text = "VEDD MEG A SPART!!!!!", font = ('Helvetica', 15))
                objektiv.pack()
                szines_j_win = Toplevel()
                objektiv = Label(szines_j_win, text = "VEDD MEG A SPART!!!!!", font = ('Helvetica', 15))
                objektiv.pack()

szines_j_ablak = Tk()
szines_j_ablak.title("Színes játék")
szines_j_ablak.minsize(width = 600, height = 400)
szines_j_ablak.maxsize(width = 600, height = 400)

objektiv = Label(szines_j_ablak, text = "Írd be, hogy milyen színűek a betűk, és nem azt, amit kiír!", font = ('Helvetica', 15))
objektiv.pack()
pontszam_label = Label(szines_j_ablak, text = "Nyomj egy \"enter\"-t a játék kezdéséért!", font = ('Helvetica', 12))
pontszam_label.pack()
ido_label = Label(szines_j_ablak, text = "Idő hátra: " + str(ido_hatra), font = ('Helvetica', 13))
ido_label.pack()
label = Label(szines_j_ablak, font = ('Helvetica', 16))
label.pack()
enter_beker = Entry(szines_j_ablak)
szines_j_ablak.bind('<Return>', jatekKezdes)
enter_beker.pack()
enter_beker.focus_set()


szines_j_ablak.mainloop()