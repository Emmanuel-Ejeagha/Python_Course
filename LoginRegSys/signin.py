#!/usr/bin/python3

import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox
import pymysql


# The Forgot password window that assists user to recover forgotten password
def forgot_passwd():
    """The forgot password window"""
    def change_password():
        """Changes the password and connects to the database"""
        if userEntry.get() == '' or new_passwordEntry.get() == '' or con_passwordEntry.get() == '':
            messagebox.showerror('Error', 'All Fields Are Required', parent=window)
        elif new_passwordEntry != con_passwordEntry:
            messagebox.showerror('Error', 'Password and Confirm Password are not matching', parent=window)
        else:
            con = pymysql.connect(
                host='localhost',
                user='backend-developer',
                password='StrongPassword123!',
                port=3306,
                database='userdata'
            )
            mycursor = con.cursor()
            query = 'SELECT * FROM data WHERE userdata=%s'
            mycursor.execute(query, (userEntry.get()))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error', 'Incorrect Username', parent=window)
            else:
                query = 'UPDATE data SET password=%s WHERE username=%s'
                mycursor.execute(query, (new_passwordEntry.get(), userEntry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Passord is reset, please login with new password', parent=window)
                window.destroy()

    window = tk.Toplevel()
    window.title('Change Password')
    window.geometry('990x660+50+50')
    window.resizable(False, False)  # Disable window resizing

    bgpic = ImageTk.PhotoImage(file='img/bgg.jpg')
    bgLabel = tk.Label(window, image=bgpic)
    bgLabel.grid()

    frame = tk.Frame(window, bg='white')
    frame.place(x=570, y=100)

    heading_label = tk.Label(frame, text='RESET PASSWORD', font=('Arial', 20, 'bold'), bg='white', fg='sea green')
    heading_label.grid(row=0, column=0, padx=10, pady=10)

    # Email Label and Entry
    userLabel = tk.Label(frame, text='Username', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                          fg='sea green')
    userLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(30, 0))
    userEntry = tk.Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'),
                          fg='tomato', bg='white')
    userEntry.grid(row=2, column=0, sticky='w', padx=25)

    # Email Label and Entry
    new_passwordLabel = tk.Label(frame, text='New Password', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                          fg='sea green')
    new_passwordLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(30, 0))
    new_passwordEntry = tk.Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'),
                          fg='tomato', bg='white')
    new_passwordEntry.grid(row=4, column=0, sticky='w', padx=25)

    con_passwordLabel = tk.Label(frame, text='Confirm Password', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                          fg='sea green')
    con_passwordLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(30, 0))
    con_passwordEntry = tk.Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'),
                          fg='tomato',  bg='white')
    con_passwordEntry.grid(row=6, column=0, sticky='w', padx=25)

    submit_button = tk.Button(frame, text='SUBMIT', bd=2, bg='tomato', fg='white', font=('Open Sans', 16, 'bold'),
                              activeforeground='white', activebackground='sea green', width=17, cursor='hand2', command=change_password)
    submit_button.grid(row=7, column=0, pady=(45, 40))

    window.mainloop()

# Stores user's data to the database
def login_user():
    """
    Confirms if a user meets the requirements to login to the page
    """
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')

    else:
        try:
            con = pymysql.connect(
                host='localhost',
                user='backend-developer',
                password='StrongPassword123!',
                port=3306
            )
            my_cursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Connection is not established try again')
            return
        query = 'USE userdata'
        my_cursor.execute(query)
        query = 'SELECT * FROM data WHERE username=%s and password=%s'
        my_cursor.execute(query, args=(passwordEntry.get(), usernameEntry.get()))
        row = my_cursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invalid username or password')
        else:
            messagebox.showinfo('Success', 'Login is successful')



def sign_up():
    """Closes the signup page and opens the signup page"""
    root.destroy()
    import signup
def hide():
    """Controls the open eye logo on the password field"""
    open_eye.config(file='img/closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    """Controls the open eye logo on the password field"""
    open_eye.config(file='img/openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def user_entry(event):
    """deletes the text on the username field so that
    the user can enter text on the field
    """
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, tk.END)

def passwd_entry(event):
    """deletes the text on the password field so that
    the user can enter text on the field
    """
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, tk.END)

root = tk.Tk()
bgImage = ImageTk.PhotoImage(file="img/bgg.jpg")
root.geometry('990x660+50+50')
root.resizable(False, False)  # Disable window resizing

# root.resizable(width=0, height=0)
root.title("Login Page")
bgLabel = tk.Label(root, image=bgImage)
bgLabel.pack(fill="both", expand=True)


heading = tk.Label(root, text='User Login', font=("Arial", 30, 'bold'), bg='#CCCCCC', fg='firebrick1')
heading.place(x=578, y=120)

usernameEntry = tk.Entry(root, width=25, font=("Arial", 17, 'bold'), bg='white', fg='firebrick1')
usernameEntry.place(x=578, y=200)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', user_entry)

frame1 = tk.Frame(root, width=330, height=2, bg='firebrick1')
frame1.place(x=580, y=232)

passwordEntry = tk.Entry(root, width=25, font=("Arial", 17, 'bold'), bg='white', fg='firebrick1')
passwordEntry.place(x=578, y=260)
passwordEntry.insert(index=0, string='Password')
passwordEntry.bind('<FocusIn>', passwd_entry)

frame1 = tk.Frame(root, width=330, height=2, bg='firebrick1')
frame1.place(x=580, y=290)

open_eye = tk.PhotoImage(file='img/openeye.png')
eyeButton = tk.Button(root, image=open_eye, bg='white', bd=0, activebackground='white',
                      cursor='hand2', command=hide)
eyeButton.place(x=886, y=262)

forgotButton = tk.Button(root, text="Forgot Password?", bd=0, bg='white', activebackground='white',
                         cursor='hand2', font=("Arial", 9, 'bold'),
                         fg='firebrick1', activeforeground='firebrick1', command=forgot_passwd)
forgotButton.place(x=786, y=295)

loginButton = tk.Button(root, text="Login", activebackground='firebrick1',
                        cursor='hand2', font=("Open Sans", 16, 'bold'),
                        fg='white', bg='firebrick1', activeforeground='white',
                        bd=0, width=21, command=login_user)
loginButton.place(x=578, y=350)

orLabel = tk.Label(root, text='---------------- OR ----------------', font=("Open Sans", 16, 'bold'), bg='white',
                   fg='firebrick1')
orLabel.place(x=578, y=400)

facebook_logo = tk.PhotoImage(file='img/facebook.png')
fbLabel = tk.Label(root, image=facebook_logo, bg='white')
fbLabel.place(x=680, y=440)

google_logo = tk.PhotoImage(file='img/google.png')
googleLabel = tk.Label(root, image=google_logo, bg='white')
googleLabel.place(x=730, y=440)

twitter_logo = tk.PhotoImage(file='img/twitter.png')
twitterLabel = tk.Label(root, image=twitter_logo, bg='white')
twitterLabel.place(x=780, y=440)

signupLabel = tk.Label(root, text='Don\'t have account?', font=("Open Sans", 9, 'bold'), fg='firebrick1', bg='white')
signupLabel.place(x=578, y=500)

new_acc_Button = tk.Button(root, text="Create new one", activebackground='white',
                            cursor='hand2', font=("Open Sans", 9, 'bold'),
                            fg='blue', bg='white', activeforeground='blue',
                            bd=0, command=sign_up)
new_acc_Button.place(x=782, y=497)

root.mainloop()
