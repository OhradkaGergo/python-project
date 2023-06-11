from tkinter import *
import random

def szinjatek(masterwindow):
    szines_j_ablak = Toplevel(masterwindow)
    szines_j_ablak.title("Színes játék")
    szines_j_ablak.minsize(width = 600, height = 400)
    szines_j_ablak.maxsize(width = 600, height = 400)

    menusor = Frame(szines_j_ablak, width=600, height=400, bd=10, highlightbackground="green", highlightthickness=10)
    menusor.pack(side = TOP, fill = X)

    menu1 = Menubutton(menusor, text = "Főoldal", underline = 0, bg="#EC4949", width=15, height=2)
    menu1.pack(side = LEFT)
    dashboard = Menu(menu1,tearoff="off")
    menu1.config(menu = dashboard)

    menu3 = Menubutton(menusor, text = "Benzin számító", underline = 0,bg="#EC4949", width=15, height=2)
    menu3.pack(side = LEFT)
    likes = Menu(menu3, tearoff="off")
    likes  .add_command(label = "Benzin", underline = 0, background="#EC4949")
    likes.add_command(label = "Diesel", underline = 0,background="#EC4949")
    menu3.config(menu = likes)

    menu2 = Menubutton(menusor, text = "Adószámító", underline = 0,bg="#EC4949", width=15, height=2)
    menu2.pack(side = LEFT)
    views = Menu(menu2, tearoff="off")
    views.add_command(label = "Adószámító", underline = 0, background="#EC4949")
    views.add_command(label = "Kenyérszámító", underline = 0,background="#EC4949")
    menu2.config(menu =views)

    menu4 = Menubutton(menusor, text = "Spar", underline = 0,bg="#EC4949", width=15, height=2)
    menu4.pack(side = LEFT)
    uploads = Menu(menu4 ,tearoff="off")

    uploads.add_command(label = "Hőmérséklet váltó", underline = 0, background="#EC4949")
    uploads.add_command(label = "Pénznem váltó", underline = 0,background="#EC4949")
    uploads.add_command(label = "Mértékegység váltó", underline = 0,background="#EC4949")
    uploads.add_command(label = "Terület/Kerület", underline = 0, background="#EC4949")
    uploads.add_command(label = "URL rövidítő", underline = 0,background="#EC4949")
    uploads.add_command(label = "Jelszó erősség",  underline = 0,background="#EC4949")

    menu4.config(menu = uploads)

    menu5 = Menubutton(menusor, text = "Játékok", underline = 0,bg="#EC4949", width=15, height=2)
    menu5.pack(side = LEFT)
    videos = Menu(menu5,tearoff="off")
    videos.add_command(label = "Színes játék", underline = 0, background="#EC4949")
    videos.add_command(label = "Vízesés modell quiz", underline = 0,background="#EC4949")

    menu5.config(menu = videos)

    menu6 = Menubutton(menusor, text = "Kilépés", underline = 0,bg="#EC4949", width=15, height=2)
    menu6.pack(side = LEFT)
    videos = Menu(menu6,tearoff="off", )
    videos.add_command(label = "Kilépés", command = szines_j_ablak.destroy, underline = 0,background="#EC4949")
    menu6.config(menu = videos)

    ize2=Label(text="Sponsored by SPAR ™", fg="green",font=('Silkscreen', 8))
    ize2.place(x=30,y=350)

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