import tkinter as tk
from PIL import ImageTk

signup = tk.Tk()
signup.title("Sign up")
signup.geometry('990x660+50+50')
signup.resizable(False, False)
background = ImageTk.PhotoImage(file='img/bgg.jpg')
bgLable = tk.Label(signup, image=background)
bgLable.grid()

# bg='#CCCCCC'
frame = tk.Frame(signup, bg='white')
frame.place(x=578, y=100)
heading = tk.Label(frame, text='Sign up', font=("Arial", 30, 'bold'), bg='white', fg='firebrick1')
heading.grid(row=0, column=0, padx=10, pady=10)

emailLabel = tk.Label(frame, text='Email', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white'
                      , fg='firebrick1')
emailLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(10, 0))

emailEntry = tk.Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'),
                      fg='white', bg='firebrick1')
emailEntry.grid(row=2, column=0, sticky='w', padx=25)

#
userLabel = tk.Label(frame, text='Username', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white'
                      , fg='firebrick1')
userLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10, 0))

userEntry = tk.Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'),
                      fg='white', bg='firebrick1')
userEntry.grid(row=4, column=0, sticky='w', padx=25)

#
passwordLabel = tk.Label(frame, text='Password', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white'
                      , fg='firebrick1')
passwordLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10, 0))

passwordEntry = tk.Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'),
                      fg='white', bg='firebrick1')
passwordEntry.grid(row=6, column=0, sticky='w', padx=25)

#
conPasswdLabel = tk.Label(frame, text='Confirm Password', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white'
                      , fg='firebrick1')
conPasswdLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10, 0))

conPasswdEntry = tk.Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'),
                      fg='white', bg='firebrick1')
conPasswdEntry.grid(row=8, column=0, sticky='w', padx=25)

#
term_and_con = tk.Checkbutton(frame, text="I agree to the terms and conditions", font=('Microsoft Yahei UI Light', 10, 'bold'),
               fg='firebrick1', bg='white', activebackground='white', activeforeground='firebrick1',
               cursor='hand2')
term_and_con.grid(row=9, column=0, pady=10, padx=25)

signupButton = tk.Button(frame, text='Signup', width=17,  font=('Open Sans', 16, 'bold'), bg='firebrick1', fg='white',
                         bd=0, activeforeground='white', activebackground='firebrick1', cursor='hand2')
signupButton.grid(row=10, column=0, pady=10)

#
alreadyAccount = tk.Label(frame, text="Don't have an account?", font=('Open Sans', 9, 'bold'),
                          bg='white', fg='firebrick1')
alreadyAccount.grid(row=11, column=0, sticky='w', padx=25, pady=10)

#
loginButton = tk.Button(frame, text='Log in', font=('Open Sans', 9, 'bold underline'), bg='white', bd=0, fg='blue',
                        cursor='hand2', activebackground='white', activeforeground='blue')
loginButton.place(x=220, y=390)

signup.mainloop()