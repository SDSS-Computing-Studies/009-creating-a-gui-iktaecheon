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

label1.grid(row=1, column=2, rowspan=3, columnspan=2)
label2.grid(row=2, column=3, columnspan=2)
label3.grid(row=4, column=2, columnspan=3)
label4.grid(row=5, column=2, columnspan=3)

window.mainloop()