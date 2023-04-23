import tkinter as tk

# create main window
root = tk.Tk()
root.title("MindCare")

# set window size
root.geometry("300x200")

# define button functions
def happy():
    print("I'm happy!")

def ok():
    print("I'm ok.")

def sad():
    print("I'm sad.")

# create buttons with proper spacing and coloring
happy_btn = tk.Button(root, text="Happy", bg="green", fg="white", padx=20, pady=10, command=happy)
ok_btn = tk.Button(root, text="Ok", bg="orange", fg="white", padx=20, pady=10, command=ok)
sad_btn = tk.Button(root, text="Sad", bg="red", fg="white", padx=20, pady=10, command=sad)

# add buttons to the window
happy_btn.pack(side=tk.LEFT, padx=20, pady=20)
ok_btn.pack(side=tk.LEFT, padx=20, pady=20)
sad_btn.pack(side=tk.LEFT, padx=20, pady=20)

# run the GUI application
root.mainloop()
