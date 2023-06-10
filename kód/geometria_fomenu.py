from tkinter import *
from geometria_kivalaszto_haromszog import haromszog
from geometria_kivalaszto_teglalap import teglalap
from geometria_kivalaszto_negyzet import negyzet
from geometria_kivalaszto_kor import kor

def handoff(id): 
    if id == 1:
        haromszog(geoablak)
    elif id == 2:
        teglalap(geoablak)
    elif id == 3:
        negyzet(geoablak)
    elif id == 4:
        kor(geoablak)

def drawtriangle():
    print(selection.get())
    confirmbutton = Button(geoablak, text="Kiválasztás", command=lambda: handoff(1))
    confirmbutton.place(x=250, y=320)
    u149.create_rectangle(30,10,320,130, fill='black')
    u149.create_line(186, 92, 186, 25, fill="white", width=5)
    u149.create_line(109, 91, 187, 25, fill="white", width=5)
    u149.create_line(110, 90, 188, 90, fill="white", width=5)


def drawbrick():
    print(selection.get())
    confirmbutton = Button(geoablak, text="Kiválasztás", command=lambda: handoff(2))
    confirmbutton.place(x=250, y=320)
    u149.create_rectangle(30,10,320,130, fill='black')
    u149.create_line(110, 90, 110, 35, fill="white", width=5)
    u149.create_line(108, 90, 203, 90, fill="white", width=5)
    u149.create_line(200, 90, 200, 35, fill="white", width=5)
    u149.create_line(108, 35, 203, 35, fill="white", width=5)

def drawcube():
    print(selection.get())
    confirmbutton = Button(geoablak, text="Kiválasztás", command=lambda: handoff(3))
    confirmbutton.place(x=250, y=320)
    u149.create_rectangle(30,10,320,130, fill='black')
    u149.create_line(127, 35, 186, 35, fill="white", width=5)
    u149.create_line(127, 93, 127, 33, fill="white", width=5)
    u149.create_line(127, 90, 186, 90, fill="white", width=5)
    u149.create_line(186, 33, 186, 93, fill="white", width=5)

def drawcircle():
    print(selection.get())
    confirmbutton = Button(geoablak, text="Kiválasztás", command=lambda: handoff(4))
    confirmbutton.place(x=250, y=320)
    u149.create_rectangle(30,10,320,130, fill='black')
    u149.create_oval(127,33, 186, 93, outline="white" , width=5)

geoablak = Tk()
geoablak.title("Python SPAR projekt")
geoablak.minsize(width = 600, height = 400)
geoablak.maxsize(width = 600, height = 400)
selection = IntVar()
selection.set(1)
menusor = Frame(geoablak, width=600, height=400, bd=10, highlightbackground="green", highlightthickness=10)
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
videos.add_command(label = "Kilépés", command = geoablak.destroy, underline = 0,background="#EC4949")
menu6.config(menu = videos)
ize2=Label(text="Sponsored by SPAR ™", fg="green",font=('Silkscreen', 8))
ize2.place(x=30,y=350)
can1 = Canvas(geoablak, width=10, height=10)
photo = PhotoImage(file='python-project\képek\spar-logo-1.png')
item = can1.create_image(20, 20, image = photo)
can1.place(x=150,y=350)


u149 = Canvas(geoablak, width=290, height=120) #uoooh
u149.create_rectangle(30,10,320,130, fill='black')
haromszogoption = Radiobutton(geoablak, text="Háromszög", variable=selection, value=1, command=drawtriangle)
haromszogoption.select()
drawtriangle()
teglalapoption = Radiobutton(geoablak, text="Téglalap", variable=selection, value=2, command=drawbrick)
negyszogoption = Radiobutton(geoablak, text="Négyszög", variable=selection, value=3, command=drawcube)
koroption = Radiobutton(geoablak, text="Kör", variable=selection, value=4, command=drawcircle)


haromszogoption.place(x=200,y=117)
teglalapoption.place(x=200,y=137)
negyszogoption.place(x=300, y=117)
koroption.place(x=300,y=137)
u149.place(x=130, y=170)

geoablak.mainloop()