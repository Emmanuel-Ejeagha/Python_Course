#!/usr/bin/python3

import tkinter as tk
from PIL import ImageTk

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Page")
        self.geometry('990x660+50+50')
        self.initialize_widgets()

    def initialize_widgets(self):
        # Set background image
        self.bg_image = ImageTk.PhotoImage(file="img/bgg.jpg")
        bg_label = tk.Label(self, image=self.bg_image)
        bg_label.pack(fill="both", expand=True)

        # Heading Label
        heading = tk.Label(self, text='User Login', font=("Arial", 30, 'bold'), bg='#CCCCCC', fg='firebrick1')
        heading.place(x=578, y=120)

        # Username Entry
        self.username_entry = self.create_entry(200, 'Username', user_entry)
        # Password Entry
        self.password_entry = self.create_entry(230, 'Password', passwd_entry)

        # Eye Button for password visibility
        open_eye = tk.PhotoImage(file='img/openeye.png')
        self.eye_button = tk.Button(self, image=open_eye, bg='white', bd=0, activebackground='white',
                                    cursor='hand2', command=self.toggle_password_visibility)
        self.eye_button.place(x=886, y=262)

        # Other buttons and labels
        self.create_button("Forgot Password?", 295)
        self.create_button("Login", 350, width=21)
        self.create_separator(400)
        self.create_social_media_icons(440)
        self.create_button("Don't have account?", 500, font=("Open Sans", 9, 'bold'), fg='firebrick1')
        self.create_button("Create new one", 497, font=("Open Sans", 9, 'bold'), fg='blue', activeforeground='blue')

    def create_entry(self, y_pos, placeholder, event_handler):
        # Create Entry widget
        entry = tk.Entry(self, width=25, font=("Arial", 17, 'bold'), bg='white', fg='firebrick1')
        entry.place(x=578, y=y_pos)
        entry.insert(0, placeholder)
        entry.bind('<FocusIn>', event_handler)
        return entry

    def create_button(self, text, y_pos, **kwargs):
        # Create Button widget
        button = tk.Button(self, text=text, bd=0, bg='white', activebackground='white',
                           cursor='hand2', **kwargs)
        button.place(x=578 if 'width' not in kwargs else 0, y=y_pos)
        return button

    def create_separator(self, y_pos):
        # Create separator
        frame = tk.Frame(self, width=330, height=2, bg='firebrick1')
        frame.place(x=580, y=y_pos)

    def create_social_media_icons(self, y_pos):
        # Create social media icons
        icons = ['facebook', 'google', 'twitter']
        for i, icon in enumerate(icons, start=1):
            image = tk.PhotoImage(file=f'img/{icon}.png')
            label = tk.Label(self, image=image, bg='white')
            label.place(x=680 + 50 * (i - 1), y=y_pos)

    def toggle_password_visibility(self):
        # Toggle password visibility
        if self.password_entry.cget('show') == '':
            self.password_entry.config(show='*')
            self.eye_button.config(image=self.open_eye)
            self.eye_button.config(command=self.show_password)
        else:
            self.password_entry.config(show='')
            self.eye_button.config(image=self.close_eye)
            self.eye_button.config(command=self.hide_password)

def user_entry(event):
    # Handle focus in event for username entry
    if app.username_entry.get() == 'Username':
        app.username_entry.delete(0, tk.END)

def passwd_entry(event):
    # Handle focus in event for password entry
    if app.password_entry.get() == 'Password':
        app.password_entry.delete(0, tk.END)

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
