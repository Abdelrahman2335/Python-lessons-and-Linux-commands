#Creating clock

from tkinter import Tk
from tkinter import Label
import time
# import sys


master = Tk()
master.title("Digital clock")

def get_time():
    timevar = time.strftime("%D:%I:%M:%S:%p")
    clock.config(text=timevar)
    clock.after(200,get_time)

clock = Label(master,font=("Calibri",20),bg="black",fg="white")
clock.pack()


get_time()
master.mainloop()