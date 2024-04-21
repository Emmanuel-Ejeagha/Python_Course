#!/usr/bin/python3
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
import pymysql

# Clears the entry
def clear():
    """Clears the data from the Entry"""
    emailEntry.delete(0, tk.END)
    userEntry.delete(0, tk.END)
    passwordEntry.delete(0, tk.END)
    confirmPasswdEntry.delete(0, tk.END)


# Connects to Mysql database 
def connect_database():
    """
    Connects to MySQL local server
    Confirmed whether the user has filled the form completely
    """
    if emailEntry.get() == '' or userEntry.get()=='' or passwordEntry.get()=='' or confirmPasswdEntry.get()=='':
        messagebox.showerror('Error', 'All Fields Are Required!')
    elif passwordEntry.get() != confirmPasswdEntry.get():
        messagebox.showerror('Error', 'Password Mismatch!')
    elif check.get()==0:
        messagebox.showerror('Error', 'Please Accept Terms & Conditions')
    else:
        try:
            con = pymysql.connect(
                host='localhost',
                user='backend-developer',
                password='StrongPassword123!',
                port=3306  # Specify the port if it's different from the default
            )
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue, Please Try Again')
            return
        try:
            query = 'CREATE DATABASE IF NOT EXISTS userdata'
            mycursor.execute(query)
            query = 'USE userdata'
            mycursor.execute(query)
            query = """
                CREATE TABLE data (
                id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, 
                email VARCHAR(50),
                username VARCHAR(50),
                password VARCHAR(50)
            )
            """
            mycursor.execute(query)
        except:
            mycursor.execute('USE userdata')
        query = 'SELECT * FROM data WHERE username=%s'
        mycursor.execute(query, (userEntry.get()))

        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'Username Already Exists')

        else:
            query = 'INSERT INTO data(email, username, password) values(%s, %s, %s)'
            mycursor.execute(query, (emailEntry.get(), userEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is successful')
            clear()
            signup.destroy()
            import signin


# Login Page
def login_page():
    """Takes the user to the login page"""
    signup.destroy()
    import signin
    
    
# Create the Tkinter window for sign up
signup = tk.Tk()
signup.title("Sign up")
signup.geometry('990x660+50+50')  # Set window size and position
signup.resizable(False, False)  # Disable window resizing

# Load background image
background = ImageTk.PhotoImage(file='img/bgg.jpg')
bgLabel = tk.Label(signup, image=background)  # Display background image
bgLabel.grid()

# Frame for sign up form
frame = tk.Frame(signup, bg='white')  # Create a frame with white background
frame.place(x=578, y=100)  # Position the frame

# Sign up heading
heading = tk.Label(frame, text='Sign up', font=("Arial", 30, 'bold'), bg='white', fg='firebrick1')
heading.grid(row=0, column=0, padx=10, pady=10)

# Email Label and Entry
emailLabel = tk.Label(frame, text='Email', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                      fg='firebrick1')
emailLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(10, 0))
emailEntry = tk.Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'),
                      fg='white', bg='firebrick1')
emailEntry.grid(row=2, column=0, sticky='w', padx=25)

# Username Label and Entry
userLabel = tk.Label(frame, text='Username', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                     fg='firebrick1')
userLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10, 0))
userEntry = tk.Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'),
                     fg='white', bg='firebrick1')
userEntry.grid(row=4, column=0, sticky='w', padx=25)

# Password Label and Entry
passwordLabel = tk.Label(frame, text='Password', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                          fg='firebrick1')
passwordLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10, 0))
passwordEntry = tk.Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'),
                         fg='white', bg='firebrick1')
passwordEntry.grid(row=6, column=0, sticky='w', padx=25)

# Confirm Password Label and Entry
confirmPasswdLabel = tk.Label(frame, text='Confirm Password', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                          fg='firebrick1')
confirmPasswdLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10, 0))
confirmPasswdEntry = tk.Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'),
                          fg='white', bg='firebrick1')
confirmPasswdEntry.grid(row=8, column=0, sticky='w', padx=25)

# Terms and Conditions Checkbutton
check = tk.IntVar()
term_and_con = tk.Checkbutton(frame, text="I agree to the terms and conditions",
                               font=('Microsoft Yahei UI Light', 9, 'bold'),
                               fg='firebrick1', bg='white', activebackground='white',
                               activeforeground='firebrick1', cursor='hand2', variable=check)
term_and_con.grid(row=9, column=0, pady=10, padx=25)

# Signup Button
signupButton = tk.Button(frame, text='Signup', width=17, font=('Open Sans', 16, 'bold'), bg='firebrick1',
                         fg='white', bd=0, activeforeground='white', activebackground='firebrick1',
                         cursor='hand2', command=connect_database)
signupButton.grid(row=10, column=0, pady=10)

# Already have an account Label
alreadyAccount = tk.Label(frame, text="Don't have an account?", font=('Open Sans', 9, 'bold'),
                          bg='white', fg='firebrick1')
alreadyAccount.grid(row=11, column=0, sticky='w', padx=25, pady=10)

# Login Button
loginButton = tk.Button(frame, text='Log in', font=('Open Sans', 9, 'bold underline'), bg='white', bd=0, fg='blue',
                        cursor='hand2', activebackground='white', activeforeground='blue', command=login_page)
loginButton.place(x=220, y=390)


# The main loop
signup.mainloop()
