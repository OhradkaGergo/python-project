from tkinter import *

def homer_valt(masterwindow):
    def cel_fah():
        celsius = float(homerseklet_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        atvaltott_entry.delete(0, END)
        atvaltott_entry.insert(END, fahrenheit)

    def fah_cel():
        fahrenheit = float(homerseklet_entry.get())
        celsius = (fahrenheit - 32) * 5/9
        atvaltott_entry.delete(0, END)
        atvaltott_entry.insert(END, celsius)

    foablak = Toplevel()
    foablak.title("Hőmérséklet váltó")
    foablak.minsize(width = 600, height = 400)
    foablak.maxsize(width = 600, height = 400)

    menusor = Frame(foablak, width=600, height=400, bd=10, highlightbackground="green", highlightthickness=10)
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
    videos.add_command(label = "Kilépés", command = foablak.destroy, underline = 0,background="#EC4949")
    menu6.config(menu = videos)

    ize2=Label(text="Sponsored by SPAR ™", fg="green",font=('Silkscreen', 8))
    ize2.place(x=30,y=350)

    homerseklet_label = Label(foablak, text="Írd be a hőmérsékletet:", font = ('Helvetica', 10))
    homerseklet_label.pack()

    homerseklet_entry = Entry(foablak, font = ('Helvetica', 11))
    homerseklet_entry.pack()

    atv_frame = Frame(foablak)
    atv_frame.pack()

    celsius_button = Button(atv_frame, text="°C » °F", command=cel_fah, font = ('Helvetica', 10))
    celsius_button.pack(side=LEFT)

    fahrenheit_button = Button(atv_frame, text="°F » °C", command=fah_cel, font = ('Helvetica', 10))
    fahrenheit_button.pack(side=LEFT)

    atvaltott_label = Label(foablak, text="Átváltott hőmérséklet:", font = ('Helvetica', 10))
    atvaltott_label.pack()

    atvaltott_entry = Entry(foablak, font = ('Helvetica', 11))
    atvaltott_entry.pack()

    foablak.mainloop()