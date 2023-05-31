from tkinter import *

szines_j_kezdo_ablak = Tk()
szines_j_kezdo_ablak.title("Színes játék")
szines_j_kezdo_ablak.minsize(width = 600, height = 400)
szines_j_kezdo_ablak.maxsize(width = 600, height = 400)

def ujablak():
    szines_j_ablak = Toplevel()
    szines_j_ablak.title("Színes játék")
    szines_j_ablak.minsize(width = 600, height = 400)
    szines_j_ablak.maxsize(width = 600, height = 400)

btn = Button(szines_j_kezdo_ablak, text ="aaa", command = lambda: [ujablak, szines_j_kezdo_ablak.destrtoy])
btn.pack()

mainloop()

