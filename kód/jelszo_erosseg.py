from tkinter import *
import random
import string

def jel_ero(masterwindow):
    def check_jel_ero():
        jelszo = jelszo_entry.get()
        hossz = len(jelszo)
        has_lowercase = any(c.islower() for c in jelszo)
        has_uppercase = any(c.isupper() for c in jelszo)
        has_digit = any(c.isdigit() for c in jelszo)
        has_special = any(c in string.punctuation for c in jelszo)

        if hossz >= 8 and has_lowercase and has_uppercase and has_digit and has_special:
            jel_erosseg = "VEDD MEG A SPART!!!!!!!!!!"
        elif hossz >= 6 and has_lowercase and has_uppercase and has_digit:
            jel_erosseg = "Nem rossz, de nem is jó"
        else:
            jel_erosseg = "Gyengusz, szerezz jobbat"

        eredmeny_label.config(text=f"A jelszavad: {jel_erosseg}")

    def jel_gen():
        jelszo = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=14))
        jelszo_entry.delete(0, END)
        jelszo_entry.insert(END, jelszo)

    def check_jel_ero_ablak():
        jel_ero_ablak = Toplevel(fooldal)
        jel_ero_ablak.minsize(width = 400, height = 300,)
        jel_ero_ablak.maxsize(width = 400, height = 300,)
        jel_ero_ablak.title("Jelszó erősség ellenőrző")

        jelszo_beker_label = Label(jel_ero_ablak, text="Írd be a jelszavad:", font = ('Helvetica', 11))
        jelszo_beker_label.pack()

        global jelszo_entry
        jelszo_entry = Entry(jel_ero_ablak, font = ('Helvetica', 12))
        jelszo_entry.pack()

        ellenorzes_button = Button(jel_ero_ablak, text="Ellenőrizd az erősséget!", command=check_jel_ero, font = ('Helvetica', 10))
        ellenorzes_button.pack()

        global eredmeny_label
        eredmeny_label = Label(jel_ero_ablak, font = ('Helvetica', 10))
        eredmeny_label.pack()

    def jel_gen_ablak():
        generator_ablak = Toplevel(fooldal)
        generator_ablak.minsize(width = 400, height = 300,)
        generator_ablak.maxsize(width = 400, height = 300,)
        generator_ablak.title("Jelszó generátor")

        global jelszo_entry
        jelszo_entry = Entry(generator_ablak, font = ('Helvetica', 12))
        jelszo_entry.pack()

        jel_generator_button = Button(generator_ablak, text="Generáld a jelszót!", command=jel_gen, font = ('Helvetica', 10))
        jel_generator_button.pack()

    fooldal = Toplevel()
    fooldal.minsize(width = 600, height = 400,)
    fooldal.maxsize(width = 600, height = 400,)
    fooldal.title("Jelszó erősség és jelszó generátor")

    menusor = Frame(fooldal, width=600, height=400, bd=10, highlightbackground="green", highlightthickness=10)
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
    videos.add_command(label = "Kilépés", command = fooldal.destroy, underline = 0,background="#EC4949")
    menu6.config(menu = videos)

    ize2=Label(text="Sponsored by SPAR ™", fg="green",font=('Silkscreen', 8))
    ize2.place(x=30,y=350)

    jel_ero_button = Button(fooldal, text="Jelszó erősség ellenőrző", command=check_jel_ero_ablak, font = ('Helvetica', 10))
    jel_ero_button.pack()

    generator_button = Button(fooldal, text="Jelszó generátor", command=jel_gen_ablak, font = ('Helvetica', 10))
    generator_button.pack()

    fooldal.mainloop()