import tkinter as tk
from Backend import Emotions

emotions = Emotions()

# create main window
root = tk.Tk()
root.title("MindCare")

# set window size
root.geometry("1200x200")

# define button functions
def happy():
    print(emotions.get_quote("happy"))
    happyQuote = emotions.get_quote("happy")
    quote_label.config(text=happyQuote)

def ok():
    print(emotions.get_quote("ok"))
    okQuote = emotions.get_quote("ok")
    quote_label.config(text=okQuote)

def sad():
    print(emotions.get_quote("sad"))
    sadQuote = emotions.get_quote("sad")
    quote_label.config(text=sadQuote)

# create buttons with proper spacing and coloring
happy_btn = tk.Button(root, text="Happy", bg="green", fg="white", padx=20, pady=10, command=happy)
ok_btn = tk.Button(root, text="Ok", bg="orange", fg="white", padx=20, pady=10, command=ok)
sad_btn = tk.Button(root, text="Sad", bg="red", fg="white", padx=20, pady=10, command=sad)
quote_label = tk.Label(root, text="", font=("Helvetica", 12), anchor="center", justify="center")


# add buttons to the window
happy_btn.pack(side=tk.LEFT, padx=20, pady=20)
ok_btn.pack(side=tk.LEFT, padx=20, pady=20)
sad_btn.pack(side=tk.LEFT, padx=20, pady=20)
quote_label.pack(pady=10)

# run the GUI application
root.mainloop()
