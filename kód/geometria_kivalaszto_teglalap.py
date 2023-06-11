from tkinter import *
from geometria_teglalap_terulet import teglalapterulet
from geometria_teglalap_kerulet import teglalapkerulet

#u149.create_rectangle(30,10,320,130, fill='black')
#Y height: 120
#X width: 290 (145)
def teglalap(masterwindow):
    def handoff(id): 
        if id == 1:
            teglalapterulet(teglaselect)
        elif id == 2:
            teglalapkerulet(teglaselect)

    def drawbrick():
        u149.create_rectangle(20, 40, 130, 110, fill="green", outline="blue")
        u149.create_rectangle(190, 40, 300, 110, outline="blue")

    def drawt():
        confirmbutton = Button(teglaselect, text="Kiválasztás", command=lambda: handoff(1))
        confirmbutton.place(x=250, y=320)


    def drawk():
        confirmbutton = Button(teglaselect, text="Kiválasztás", command=lambda: handoff(2))
        confirmbutton.place(x=250, y=320)

    teglaselect = Toplevel(masterwindow, height=400, width=600)
    teglaselect.title("Python SPAR projekt")
    teglaselect.minsize(width = 600, height = 400)
    teglaselect.maxsize(width = 600, height = 400)
    selection = IntVar()
    selection.set(1)
    menusor = Frame(teglaselect, width=600, height=400, bd=10, highlightbackground="green", highlightthickness=10)
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
    videos.add_command(label = "Kilépés", command = teglaselect.destroy, underline = 0,background="#EC4949")
    menu6.config(menu = videos)
    ize2=Label(teglaselect, text="Sponsored by SPAR ™", fg="green",font=('Silkscreen', 8))
    ize2.place(x=30,y=350)
    can1 = Canvas(teglaselect, width=10, height=10)
    photo = PhotoImage(file='python-project\képek\spar-logo-1.png')
    can1.create_image(20, 20, image = photo)
    can1.place(x=150,y=350)


    u149 = Canvas(teglaselect, width=305, height=130) #uoooh
    teruletoption = Radiobutton(teglaselect, text="Terület", variable=selection, value=1, command=drawt)
    teruletoption.select()
    keruletoption = Radiobutton(teglaselect, text="Kerület", variable=selection, value=2, command=drawk)
    drawbrick()
    drawt()


    teruletoption.place(x=175,y=117)
    keruletoption.place(x=340,y=117)
    u149.place(x=130, y=135)

    teglaselect.mainloop()