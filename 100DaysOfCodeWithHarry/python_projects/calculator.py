#!/usr/bin/python3
import tkinter as tk

# Global variable to store the calculation expression
calculation = ""

# Function to add symbols to the calculation expression
def add_cal(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

# Function to evaluate the calculation expression
def evaluate_cal():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

# Function to clear the calculation field
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Set window resizable
window.resizable(True, True)

# Create text widget to display calculation
text_result = tk.Text(window, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5, sticky="nsew")

# Define button labels and positions
button_labels = [
    ("1", 2, 1), ("2", 2, 2), ("3", 2, 3), ("4", 3, 1),
    ("5", 3, 2), ("6", 3, 3), ("7", 4, 1), ("8", 4, 2),
    ("9", 4, 3), ("0", 5, 2), ("+", 2, 4), ("-", 3, 4),
    ("*", 4, 4), ("/", 5, 4), ("(", 5, 1), (")", 5, 3)
]

# Create buttons and place them on the grid
buttons = []
for label, row, column in button_labels:
    button = tk.Button(window, text=label, command=lambda label=label: add_cal(label), font=("Arial", 14))
    button.grid(row=row, column=column, sticky="nsew")
    buttons.append(button)

window.title("Simple Calculator")
# Create equal and clear buttons
buttonEqual = tk.Button(window, text="=", command=evaluate_cal, font=("Arial", 14))
buttonEqual.grid(row=6, column=3, columnspan=2, sticky="nsew")

buttonClear = tk.Button(window, text="C", command=clear_field, font=("Arial", 14))
buttonClear.grid(row=6, column=1, columnspan=2, sticky="nsew")

# Configure grid to resize buttons with window
for i in range(7):
    window.grid_rowconfigure(i, weight=1)
for i in range(5):
    window.grid_columnconfigure(i, weight=1)

# Start the GUI event loop
window.mainloop()
