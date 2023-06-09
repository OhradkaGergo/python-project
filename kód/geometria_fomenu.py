from tkinter import *

def draw(id):
    if id == 1:
        canvas.create_line(165, 75, 165, 25, fill="blue", width=5)
        canvas.create_line(100, 75, 165, 25, fill="blue", width=5)
        canvas.create_line(100, 75, 165, 75, fill="blue", width=5)
        return 
    elif id == 2:
        canvas.create_line(165, 75, 165, 25, fill="blue", width=5)
        canvas.create_line(100, 75, 165, 25, fill="blue", width=5)
        canvas.create_line(100, 75, 165, 75, fill="blue", width=5)
        return
    elif id == 3:
        canvas.create_line(165, 75, 165, 25, fill="blue", width=5)
        canvas.create_line(100, 75, 165, 25, fill="blue", width=5)
        canvas.create_line(100, 75, 165, 75, fill="blue", width=5)
        return
    elif id == 4:
        canvas.create_line(165, 75, 165, 25, fill="blue", width=5)
        canvas.create_line(100, 75, 165, 25, fill="blue", width=5)
        canvas.create_line(100, 75, 165, 75, fill="blue", width=5)
        return


geoablak = Tk()
geoablak.title("Python SPAR projekt")
geoablak.minsize(width = 600, height = 400)
geoablak.maxsize(width = 600, height = 400)
selection = IntVar()

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
photo = PhotoImage(file='python-project\képek\spar-logo-1.png',)
item = can1.create_image(20, 20, image = photo)
can1.place(x=150,y=350)


haromszogoption = Radiobutton(geoablak, text="Háromszög", variable=selection, value=1, command=draw(1))
teglalapoption = Radiobutton(geoablak, text="Téglalap", variable=selection, value=2, command=draw(2))
negyszogoption = Radiobutton(geoablak, text="Négyszög", variable=selection, value=3, command=draw(3))
koroption = Radiobutton(geoablak, text="Kör", variable=selection, value=4, command=draw(4))
global canvas
canvas = Canvas(geoablak, width=290, height=120)
canvas.create_rectangle(30,10,320,130, fill='black')


haromszogoption.place(x=200,y=137)
teglalapoption.place(x=200,y=117)
negyszogoption.place(x=300, y=137)
koroption.place(x=300,y=117)
canvas.place(x=130, y=170)


geoablak.mainloop()