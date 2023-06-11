from tkinter import *

def atvaltas():
    try:
        ertek = float(entry_ertek.get())
        opcio = combobox_unit.get()

        if opcio == "Milliméter > Centiméter":
            result = ertek / 10
        elif opcio == "Centiméter > Milliméter":
            result = ertek * 10
        elif opcio == "Centiméter > Deciméter":
            result = ertek / 10
        elif opcio == "Deciméter > Centiméter":
            result = ertek * 10
        elif opcio == "Deciméter > Méter":
            result = ertek / 10
        elif opcio == "Méter > Deciméter":
            result = ertek * 10
        elif opcio == "Méter > Kilóméter":
            result = ertek / 1000
        elif opcio == "Kilóméter > Méter":
            result = ertek * 1000
        else:
            raise ValueError("Rossz!")

        entry_eredmeny.delete(0, END)
        entry_eredmeny.insert(0, result)
    except ValueError:
        entry_eredmeny.delete(0, END)
        entry_eredmeny.insert(0, "Rossz!")

mert_egy_ablak = Tk()
mert_egy_ablak.title("Mértékegység átváltó")
mert_egy_ablak.minsize(width = 600, height = 400)
mert_egy_ablak.maxsize(width = 600, height = 400)

menusor = Frame(mert_egy_ablak, width=600, height=400, bd=10, highlightbackground="green", highlightthickness=10)
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
videos.add_command(label = "Kilépés", command = mert_egy_ablak.destroy, underline = 0,background="#EC4949")
menu6.config(menu = videos)

ize2=Label(text="Sponsored by SPAR ™", fg="green",font=('Silkscreen', 8))
ize2.place(x=30,y=350)

frame = Frame(mert_egy_ablak)
frame.pack(pady=20)

label_ertek = Label(frame, text = "Írd be a mennyiséget:", font = ('Helvetica', 12))
label_ertek.pack()
entry_ertek = Entry(frame, width = 10)
entry_ertek.pack()

atvaltas_opciok = [
    "Milliméter > Centiméter",
    "Centiméter > Milliméter",
    "Centiméter > Deciméter",
    "Deciméter > Centiméter",
    "Deciméter > Méter",
    "Méter > Deciméter",
    "Méter > Kilóméter",
    "Kilóméter > Méter"
]
combobox_unit = StringVar(mert_egy_ablak)
combobox_unit.set(atvaltas_opciok[0])
combobox = OptionMenu(frame, combobox_unit, *atvaltas_opciok)
combobox.pack(pady=10)

atvalto_gomb = Button(frame, text= "Átváltás!", command = atvaltas, font = ('Helvetica', 10))
atvalto_gomb.pack()

label_eredmeny = Label(frame, text = "Eredmény:", font = ('Helvetica', 12))
label_eredmeny.pack()
entry_eredmeny = Entry(frame, width = 10)
entry_eredmeny.pack()

mert_egy_ablak.mainloop()