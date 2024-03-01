#!/usr/bin/python3
# This script displays a digital clock

from time import strftime
from tkinter import Label, Tk

# Window config for clock
window = Tk()
window.title("")
window.geometry("300x80")
window.configure(bg="blue")
window.resizable(False,False)

# Label config
clock_label = Label(window, bg="blue", fg="yellow", font=("Times", 30, "bold"), relief="flat")
clock_label.place(x = 20, y = 20)

def updating_label():
    current_time = strftime('%H, %M, %S')
    clock_label.configure(text=current_time)
    clock_label.after(80, updating_label)

updating_label()
window.mainloop()
