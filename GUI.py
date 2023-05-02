import tkinter as tk
import pygame
from Backend import Emotions
import customtkinter as ctk
import tkinter.messagebox as tkmb

class LoginUI:
    def __init__(self):
        # Selecting GUI theme - dark, light , system (for system default)
        ctk.set_appearance_mode("dark")

        # Selecting color theme - blue, green, dark-blue
        ctk.set_default_color_theme("blue")

        self.app = ctk.CTk()
        self.app.geometry("500x550")
        self.app.title("Modern Login UI using Customtkinter")

        label = ctk.CTkLabel(self.app, text="This is the main UI page")
        label.pack(pady=20)

        frame = ctk.CTkFrame(master=self.app)
        frame.pack(pady=20, padx=40, fill='both', expand=True)

        label = ctk.CTkLabel(master=frame, text='Modern Login System UI')
        label.pack(pady=12, padx=10)

        self.user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
        self.user_entry.pack(pady=12, padx=10)

        self.pass_entry = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
        self.pass_entry.pack(pady=12, padx=10)

        button = ctk.CTkButton(master=frame, text='Login', command=self.login)
        button.pack(pady=12, padx=10)

        register_button = ctk.CTkButton(master=frame, text='Register', command=self.show_register)
        register_button.pack(pady=12, padx=10)

        self.register_frame = ctk.CTkFrame(master=frame)

        self.register_user_entry = ctk.CTkEntry(master=self.register_frame)
        self.register_user_entry.pack(pady=12, padx=10)

        self.register_pass_entry = ctk.CTkEntry(master=self.register_frame, show="*")
        self.register_pass_entry.pack(pady=12, padx=10)

        self.register_save_button = ctk.CTkButton(self.register_frame, text='Save', command=self.save)
        self.register_save_button.pack(pady=12, padx=10)

        self.register_cancel_button = ctk.CTkButton(self.register_frame, text='Cancel', command=self.hide_register)
        self.register_cancel_button.pack(pady=12, padx=10)

        self.hide_register()

    def show_register(self):
        self.register_frame.pack(pady=12, padx=10, fill='both', expand=True)

    def hide_register(self):
        self.register_frame.pack_forget()

    def save(self):
        with open('accounts.txt', 'a') as f:
            f.write(self.register_user_entry.get() + ',' + self.register_pass_entry.get() + '\n')

        tkmb.showinfo(title="Registration Successful", message="You have registered successfully")
        self.hide_register()
        self.app.withdraw()

    def login(self):
        username = self.user_entry.get()
        password = self.pass_entry.get()
        with open('accounts.txt', 'r') as f:
            data = f.readlines()
        for line in data:
            line = line.strip().split(',')
            if line[0] == username:
                if line[1] == password:
                    tkmb.showinfo(title="Login Successful", message="You have logged in Successfully")
                    self.app.withdraw()
                    return
                else:
                    tkmb.showwarning(title='Wrong Password', message='Please check your password')
                    return
        tkmb.showerror(title='User not found', message='Please check your username')
    def run(self):
        self.app.mainloop()






class MindCare:
    def __init__(self):
        self.login = LoginUI()


    def run(self):
        self.login.run()



mindcare = MindCare()
mindcare.run()