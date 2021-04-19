import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("T-Town Veterinary Clinc Database")

button1 = tk.Button(window, text="Search by Name")
button2 = tk.Button(window,text="Previous")
button3 = tk.Button(window,text="Save Entry")
button4 = tk.Button(window,text="Next")

entry1 = tk.Entry(window, text="blank name")
entry2 = tk.Entry(window, text="name")
entry3 = tk.Entry(window, text="type")
entry4 = tk.Entry(window, text="breed")
entry5 = tk.Entry(window, text="owner")
entry6 = tk.Entry(window, text="bday")

dogphoto = PhotoImage(file="dog.png")

label1 = tk.Label(window, image=dogphoto)
label2 = tk.Label(window, text="Client Database")
label3 = tk.Label(window, text="Name")
label4 = tk.Label(window, text="Type")
label5 = tk.Label(window, text="Breed")
label6 = tk.Label(window, text="Owner")
label7 = tk.Label(window, text="Birthday")

button1.grid(row=1, column=4)
button2.grid(row=5, column=1)
button3.grid(row=5, column=5)
button4.grid(row=5, column=3)

entry1.grid(row=1, column=5)
entry2.grid(row=4, column=1)
entry3.grid(row=4, column=2)
entry4.grid(row=4, column=3)
entry5.grid(row=4, column=4)
entry6.grid(row=4, column=5)

label1.grid(row=1, column=1, rowspan=2)
label2.grid(row=2, column=3)
label3.grid(row=3, column=1)
label4.grid(row=3, column=2)
label5.grid(row=3, column=3)
label6.grid(row=3, column=4)
label7.grid(row=3, column=5)

window.mainloop()