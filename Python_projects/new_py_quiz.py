#!/usr/bin/python3
# python quiz project

import tkinter as tk
from tkinter import StringVar

root = tk.Tk()
root.geometry('500x500')
root.title("Python Quiz")

questions = [
    {
        "question": "1) What does the Python len() function do?",
        "options":[
            "A) Returns the length of a string",
            "B) Returns the length of a list",
            "C) Returns the length of a dictionary",
            "D) All of the above"
        ],
        "answer": "D"
    },
    {
        "question": "2) Which of the following statements is used to create a function in Python?",
        "options":[
            "A) func()",
            "B) def func()",
            "C) define func()",
            "D) create func()"
        ],
        "answer": "B"
    },
    {
        "question": "3) What is the result of the expression 3 * 'Python'?",
        "options":[
            "A) 'PythonPythonPython'",
            "B) 'PythonPython'",
            "C) 'Python3'",
            "D) Error"
        ],
        "answer": "A"
    },
    {
        "question": "4) Which of the following data types is mutable in Python?",
        "options":[
            "A) Tuple",
            "B) String",
            "C) List",
            "D) Set"
        ],
        "answer": "C"      
    },
    {
        "question": "5) What does the if __name__ == \"__main__\": statement do in Python?",
        "options":[
            "A) It defines the main function of the program",
            "B) It checks if the program is running on a main thread",
            "C) It checks if the module is being run as the main program",
            "D) It has no effect"
        ],
        "answer": "C"
    },
    {
        "question": "6) Which method can be used to add an item to the end of a list in Python?",
        "options":[
            "A) append()",
            "B) add()",
            "C) insert()",
            "D) extend()"
        ],
        "answer": "A"
    },
]


frame = tk.Frame(padx=10, pady=10, bg='#fff')
frame.pack(fill="both", expand=True)

question_label = tk.Label(frame, height=5, width=28, bg='grey', fg='#fff', font=('Veedana', 20), wraplength=500)
question_label.grid(row=0, column=0)

button_next = tk.Button(frame, text='Next', bg='orange', font=('Veedana', 20), command=lambda: displayNextQuestion())
button_next.grid(row=6, column=0, sticky='s')

v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)

option1 = tk.Radiobutton(frame, bg='#fff', variable=v1, font=('Veedana', 20), command=lambda: checkAnswer(option1))
option2 = tk.Radiobutton(frame, bg='#fff', variable=v2, font=('Veedana', 20), command=lambda: checkAnswer(option2))
option3 = tk.Radiobutton(frame, bg='#fff', variable=v3, font=('Veedana', 20), command=lambda: checkAnswer(option3))
option4 = tk.Radiobutton(frame, bg='#fff', variable=v4, font=('Veedana', 20), command=lambda: checkAnswer(option4))

option1.grid(row=2, column=0, sticky='w')
option2.grid(row=3, column=0, sticky='w')
option3.grid(row=4, column=0, sticky='w')
option4.grid(row=5, column=0, sticky='w')

index = 0
correct = 0
# create a function to disable radiobuttons
def disableButtons(state):
    # option1['state'] = state
    # option2['state'] = state
    # option3['state'] = state
    # option4['state'] = state
    pass

# create a function to check the selected answer
def checkAnswer(radio):
    global correct, index
    
    # the 4th item is the correct answer
    # we will check the user selected anser with the 4th item
    if radio['text'] == questions[index][4]:
        correct += 1
    
    index += 1
    disableButtons('disable')
    
# create a function to display the next question
def displayNextQuestion():
    global index, correct
    
    if button_next['text'] == 'Restart The Quiz':
        question_label['bg'] = 'grey'
        button_next['text'] = 'Next'
        
    elif index == len(questions):
        question_label['text'] = str(correct) + "/" + str(len(questions))
        button_next['text'] = "Restart The Quiz"
        if correct >= len(questions)/2:
            question_label['bg'] = 'sea green'
        else:
            question_label['bg'] = 'red'
    
    else:
        question_label['text'] = questions[index]['question']
        
        disableButtons('enable')
        opts = questions[index]["options"]
        option1['text'] = opts[0]
        option2['text'] = opts[1]
        option3['text'] = opts[2]
        option4['text'] = opts[3]
        v1.set(opts[0])
        v2.set(opts[1])
        v3.set(opts[0])
        v4.set(opts[0])
        
        if index == len(questions) - 1:
            button_next['text'] = "Check the result"
        
displayNextQuestion()
    
root.mainloop()