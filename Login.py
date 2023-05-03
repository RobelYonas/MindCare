import customtkinter as ctk
import tkinter.messagebox as tkmb

# Selecting GUI theme - dark, light , system (for system default)
ctk.set_appearance_mode("dark")

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("500x550")
app.title("Modern Login UI using Customtkinter")

def register():
    new_window = ctk.CTkToplevel(app)
    new_window.title("Register")

    new_window.geometry("500x550")

    user_label = ctk.CTkLabel(new_window, text='Enter Username:')
    user_label.pack(pady=12, padx=10)

    user_entry = ctk.CTkEntry(new_window)
    user_entry.pack(pady=12, padx=10)

    pass_label = ctk.CTkLabel(new_window, text='Enter Password:')
    pass_label.pack(pady=12, padx=10)

    pass_entry = ctk.CTkEntry(new_window, show="*")
    pass_entry.pack(pady=12, padx=10)

    def save():
        with open('accounts.txt', 'a') as f:
            f.write(user_entry.get() + ',' + pass_entry.get() + '\n')

        tkmb.showinfo(title="Registration Successful", message="You have registered successfully")
        new_window.destroy()

    save_button = ctk.CTkButton(new_window, text='Save', command=save)
    save_button.pack(pady=12, padx=10)


def login():
    username = user_entry.get()
    password = pass_entry.get()
    with open('accounts.txt', 'r') as f:
        data = f.readlines()
    for line in data:
        line = line.strip().split(',')
        if line[0] == username:
            if line[1] == password:
                tkmb.showinfo(title="Login Successful", message="You have logged in Successfully")
                app.destroy() # close the window upon successful login
                return
            else:
                tkmb.showwarning(title='Wrong Password', message='Please check your password')
                return
    tkmb.showwarning(title='Wrong Username', message='Please check your username')


label = ctk.CTkLabel(app, text="This is the main UI page")
label.pack(pady=20)

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='Modern Login System UI')
label.pack(pady=12, padx=10)

user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
user_entry.pack(pady=12, padx=10)

pass_entry = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
pass_entry.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text='Login', command=login)
button.pack(pady=12, padx=10)

register_button = ctk.CTkButton(master=frame, text='Register', command=register)
register_button.pack(pady=12, padx=10)

app.mainloop()