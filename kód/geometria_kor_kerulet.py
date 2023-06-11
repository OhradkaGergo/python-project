from tkinter import *
import math

def keruletwindow(masterwindow):
    def calc(*args):
        r = rlengthscan.get()
        res = 2 * (math.pi) * (int(r))
        results.delete(0, END)
        results.insert(0, str(res))
    kork = Toplevel(masterwindow, height=400, width=600)
    kork.title("Python SPAR projekt")
    kork.minsize(width = 600, height = 400)
    kork.maxsize(width = 600, height = 400)
    selection = IntVar()
    selection.set(1)
    rlengthscan = StringVar()
    menusor = Frame(kork, width=600, height=400, bd=10, highlightbackground="green", highlightthickness=10)
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
    videos.add_command(label = "Kilépés", command = kork.destroy, underline = 0,background="#EC4949")
    menu6.config(menu = videos)
    ize2=Label(kork, text="Sponsored by SPAR ™", fg="green",font=('Silkscreen', 8))
    ize2.place(x=30,y=350)
    can1 = Canvas(kork, width=10, height=10)
    photo = PhotoImage(file='python-project\képek\spar-logo-1.png')
    item = can1.create_image(20, 20, image = photo)
    can1.place(x=150,y=350)

    textbox = Label(kork, text="Kör Kerület", fg="green")
    r = Label(kork, text="r", fg="green")
    rlength = Entry(kork, textvariable=rlengthscan, width=35)
    rlength.focus()
    rlengthscan.trace_add("write", calc)
    results = Entry(kork, width=35)
    resulttext = Label(kork, text="Eredmény:", fg="green")


    rlength.place(x=65, y=145)
    r.place(x=45, y=145)
    textbox.place(x=60, y=115)
    results.place(x=65, y=205)
    resulttext.place(x=1, y=205)

    