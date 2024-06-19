#!/usr/bin/python3
# python quiz project

import tkinter as tk
from tkinter import StringVar

root = tk.Tk()
root.geometry('500x500')

questions = [
    {
        "question": "1) What does the Python len() function do?",
        "options":[
            "A) Returns the length of a string",
            "B) Returns the length of a list",
            "C) Returns the length of a dictionary",
            "D) All of the above"
        ]
    },
    {
        "question": "2) Which of the following statements is used to create a function in Python?",
        "options":[
            "A) func()",
            "B) def func()",
            "C) define func()",
            "D) create func()"
        ]
    }
    {
        "question": "3) What is the result of the expression 3 * 'Python'?",
        "options":[
            "A) 'PythonPythonPython'",
            "B) 'PythonPython'",
            "C) 'Python3'",
            "D) Error"
        ]
    }
    {
        "question": "4) Which of the following data types is mutable in Python?",
        "options":[
            "A) Tuple",
            "B) String",
            "C) List",
            "D) Set"
        ]       
    }
    {
        "question": "5) What does the if __name__ == \"__main__\": statement do in Python?",
        "options":[
            "A) It defines the main function of the program",
            "B) It checks if the program is running on a main thread",
            "C) It checks if the module is being run as the main program",
        ]   "D) It has no effect"
        
    }
    {
        "question": "6) Which method can be used to add an item to the end of a list in Python?",
        "options":[
            "A) append()",
            "B) add()",
            "C) insert()",
            "D) extend()"
        ]
    }
]


frame = tk.Frame(padx=10, pady=10, bg='#fff')
frame.pack(fill="both", expand="true")

question_label = tk.Label(frame, height=5, width=28, bg='#ddd', font=('Veedana', 20), wraplength=500)
question_label.grid(row=0, column=0)

option1 = tk.Radiobutton(frame, bg='#fff', font=('Veedana', 20))
option2 = tk.Radiobutton(frame, bg='#fff', font=('Veedana', 20))
option3 = tk.Radiobutton(frame, bg='#fff', font=('Veedana', 20))
option4 = tk.Radiobutton(frame, bg='#fff', font=('Veedana', 20))

option1.grid(row=1, column=0)
option2.grid(row=1, column=0)
option3.grid(row=1, column=0)
option4.grid(row=1, column=0)

button_next = tk.Button(frame, text='Next', font=('Veedana', 20))
button_next.grid(row=1, column=0)

root.mainloop()