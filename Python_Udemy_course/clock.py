#!/usr/bin/python3
# This script displays a digital clock

from time import strftime
from tkinter import Label, Tk

# Window config for clock
window = Tk()
window.title("Digital Clock")
window.geometry("400x100")
window.configure(bg="black")
window.resizable(False,False)

# Label config
clock_label = Label(window, bg="black", fg="cyan", font=("Helvetica", 48, "bold"), relief="flat")
clock_label.pack(pady=20)

def updating_label():
    current_time = strftime('%H:%M:%S')
    clock_label.configure(text=current_time)
    clock_label.after(1000, updating_label)

updating_label()
window.mainloop()
