from tkinter import *
import pyshorteners

def urlshort(masterwindow):
    url_rovidito = Toplevel(masterwindow)
    url_rovidito.title("URL Rövidítő")
    url_rovidito.minsize(width = 600, height = 400)
    url_rovidito.maxsize(width = 600, height = 400)

    urlmain = StringVar()
    urlshortmain = StringVar()

    def shorten_url():
        long_url = entry_url.get()
        shortener = pyshorteners.Shortener()
        shortened_url = shortener.tinyurl.short(long_url)
        roviditett_entry.delete(0, END)
        roviditett_entry.insert(0, shortened_url)

    menusor = Frame(url_rovidito, width=600, height=400, bd=10, highlightbackground="green", highlightthickness=10)
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
    videos.add_command(label = "Kilépés", command = url_rovidito.destroy, underline = 0,background="#EC4949")
    menu6.config(menu = videos)

    ize2=Label(text="Sponsored by SPAR ™", fg="green",font=('Silkscreen', 8))
    ize2.place(x=30,y=350)

    label_url = Label(url_rovidito, text="Írd be az URL-t:", font = ('Helvetica', 12))
    label_url.pack()

    entry_url = Entry(url_rovidito, width=70)
    entry_url.pack()

    button_rovidit = Button(url_rovidito, text="Rövidítés!", command = shorten_url, font = ('Helvetica', 12))
    button_rovidit.pack()

    roviditett_label = Label(url_rovidito, text="Itt a rövidített URL:", font = ('Helvetica', 12))
    roviditett_label.pack()

    roviditett_entry = Entry(url_rovidito, width=40)
    roviditett_entry.pack()

    url_rovidito.mainloop()