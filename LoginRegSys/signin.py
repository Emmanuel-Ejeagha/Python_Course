#!/usr/bin/python3

import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox
import pymysql

def forgot_passwd():
    window = tk.Toplevel()
    window.title('Change Password')
    window.geometry('990x660+50+50')
    window.resizable(False, False)  # Disable window resizing

    bgPic = ImageTk.PhotoImage(file='img/bgg.jpg')
    bgLabel = tk.Label(window, image=bgPic)
    bgLabel.grid()


    window.mainloop()
def login_user():
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
    root.destroy()
    import signup
def hide():
    open_eye.config(file='img/closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    open_eye.config(file='img/openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def user_entry(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, tk.END)

def passwd_entry(event):
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
