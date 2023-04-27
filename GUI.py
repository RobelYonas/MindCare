import tkinter as tk
import pygame

from Backend import Emotions

emotions = Emotions()

# initialize pygame mixer
pygame.mixer.init()

# define button functions
def happy():
    quote = emotions.get_quote("happy")
    quote_label.config(text=quote)
    play_audio()

def ok():
    quote = emotions.get_quote("ok")
    quote_label.config(text=quote)
    play_audio()

def sad():
    quote = emotions.get_quote("sad")
    quote_label.config(text=quote)
    play_audio()

def play_audio():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load("Audio-1.mp3")
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()

def pause_audio():
    pygame.mixer.music.pause()

# create main window
root = tk.Tk()
root.title("MindCare")
root.geometry("500x550")
root.resizable(False, False)

# create canvas
canvas = tk.Canvas(root, width=500, height=550, bg="#ffffff")
canvas.pack()

# create emotion buttons
happy_btn = tk.Button(canvas, text="Happy", bg="#77dd77", fg="#ffffff", font=("Helvetica", 16), padx=20, pady=10, command=happy)
ok_btn = tk.Button(canvas, text="Ok", bg="#ffa500", fg="#ffffff", font=("Helvetica", 16), padx=25, pady=10, command=ok)
sad_btn = tk.Button(canvas, text="Sad", bg="#ff6961", fg="#ffffff", font=("Helvetica", 16), padx=25, pady=10, command=sad)

# create audio buttons
play_btn = tk.Button(canvas, text="Play", bg="#77dd77", fg="#ffffff", font=("Helvetica", 16), padx=20, pady=10, command=play_audio)
pause_btn = tk.Button(canvas, text="Pause", bg="#ffa500", fg="#ffffff", font=("Helvetica", 16), padx=25, pady=10, command=pause_audio)

# create quote label
quote_label = tk.Label(canvas, text="", font=("Helvetica", 16), anchor="center", justify="center", wraplength=400)

# add buttons and quote label to canvas
canvas.create_window(250, 100, window=happy_btn)
canvas.create_window(250, 200, window=ok_btn)
canvas.create_window(250, 300, window=sad_btn)
canvas.create_window(125, 400, window=play_btn)
canvas.create_window(375, 400, window=pause_btn)
canvas.create_window(250, 475, window=quote_label)

# run the GUI application
root.mainloop()
