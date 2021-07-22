from tkinter import *
import time
from os.path import dirname, abspath
from sys import argv
from random import choice
w = Tk()
w.title("Pocket Stoic")
w.geometry('500x500')
assets = str(abspath(dirname(argv[0]))) + '/assets/'
logo = PhotoImage(file=assets+'logo.png')
pillar = PhotoImage(file=assets+'pillar.png')
w.call('wm', 'iconphoto', w._w, pillar)
time.sleep(1)
w.config(bg="#000000")
logolabel = Label(w, image=logo, highlightthickness=0, borderwidth=0)
logolabel.place(x=100, y=20)
list_of_quotes = ["Bruh1", "Oof2", "Yeet3"]
quotelabel = Label(w, fg="white", bg="black")
quotelabel.place(x=225, y=220)
b = Button(w, text="Give me a quote", command=lambda:quotelabel.config(text=choice(list_of_quotes)), bg="black", fg="white")
b.place(x=200, y=420)
w.mainloop()
