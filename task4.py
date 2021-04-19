import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Example")
dogphoto = PhotoImage(file="dog.png")

label1 = Label(window, image=dogphoto)
label2 = Label(window, text="Pochacco!")
label3 = Label(window, text="A cuffly little puppy! This is from the same ", background="#aaffff")
label4 = Label(window, text="creators who brought you keropi and kero kero", background="#aaffff")

label1.place(x=70,y=0)
label2.place(x=190,y=70)
label3.place(x=-1,y=120)
label4.place(x=60,y=160)

window.mainloop()