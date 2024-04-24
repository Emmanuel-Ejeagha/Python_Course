#!/usr/bin/python3
# python quiz project

# Import the necessary modules
import tkinter as tk
from tkinter import StringVar

# Create the main Tkinter window
root = tk.Tk()
root.geometry('800x600')
root.title("Python Quiz")

# Define the list of questions, options, and answers
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

# Initialize the index variable to keep track of the current question
index = 0 

# Create a frame for the quiz layout
frame = tk.Frame(padx=30, pady=20, bg='#fff')
frame.pack(fill="both", expand=True)

# Create a label to display the question
question_label = tk.Label(frame, height=7, width=50, bg='gray89', fg='gray12', font=('Verdana', 18), wraplength=500)
question_label.grid(row=0, column=0, sticky='w')

# Create a button for navigating to the next question or restarting the quiz
button_next = tk.Button(frame, text='Next', bg='orange', font=('Verdana', 20), command=lambda: displayNextQuestion(), fg='gray1')
button_next.grid(row=9, column=0, sticky='s')

# Create StringVar variables for the radio button options
v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)

# Create radio buttons for displaying options
option1 = tk.Radiobutton(frame, bg='#fff', variable=v1, fg='gray30', font=('Verdana', 15))
option2 = tk.Radiobutton(frame, bg='#fff', variable=v2, fg='gray30', font=('Verdana', 15))
option3 = tk.Radiobutton(frame, bg='#fff', variable=v3, fg='gray30', font=('Verdana', 15))
option4 = tk.Radiobutton(frame, bg='#fff', variable=v4, fg='gray30', font=('Verdana', 15))

# Arrange the radio buttons in the frame
option1.grid(row=2, column=0, sticky='w')
option2.grid(row=3, column=0, sticky='w')
option3.grid(row=4, column=0, sticky='w')
option4.grid(row=5, column=0, sticky='w')

# Initialize the variable to keep track of correct answers
correct = 0  

# Define a function to disable the radio buttons
def disableButtons(normal):
    option1['state'] = normal
    option2['state'] = normal
    option3['state'] = normal
    option4['state'] = normal


# Define a function to check the selected answer
def checkAnswer():
  global correct, index
  
  # Get the selected option using the selected variable of the radiobutton
  selected_option = option1.get()  # Get the value of the selected radio button

  # Compare the selected option with the correct answer
  if selected_option == questions[index]["answer"]:
      correct += 1
  
  index += 1
  disableButtons('disable')


# Define a function to display the next question
def displayNextQuestion():
    global index, correct
    
    if button_next['text'] == 'Restart The Quiz':
        correct = 0
        index = 0
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
        question_label['text'] = questions[index]["question"]
        
        disableButtons('disabled')
        opts = questions[index]["options"]
        option1['text'] = opts[0]
        option2['text'] = opts[1]
        option3['text'] = opts[2]
        option4['text'] = opts[3]
        v1.set(opts[0])
        v2.set(opts[1])
        v3.set(opts[2])
        v4.set(opts[3])
        
        if index == len(questions) - 1:
            button_next['text'] = "Check the result"
        
        index += 1

# Call the function to display the first question
displayNextQuestion()

# Start the Tkinter event loop
root.mainloop()
