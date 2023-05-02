import tkinter as tk
import pygame

from Backend import Emotions

emotions = Emotions()

# initialize pygame mixer
pygame.mixer.init()

# define button functions
def update_emotion(emotion_name):
    quote = emotions.get_quote(emotion_name.lower())
    quote_label.config(text=quote)

def play_audio():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load("Audio-1.mp3")
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()

def open_meditate_window():
    # create new window for meditation
    meditate_window = tk.Toplevel(root)
    meditate_window.title("Meditation")
    meditate_window.geometry("500x500")
    meditate_window.resizable(False, False)

    # create canvas
    canvas = tk.Canvas(meditate_window, width=500, height=500, bg="#2C3E50")
    canvas.pack()

    # create label for meditation instructions
    instructions_label = tk.Label(canvas, text="Close your eyes and focus on your breath.", font=("Helvetica", 16), anchor="center", justify="center", wraplength=400, fg="#ffffff", bg="#2C3E50")
    canvas.create_window(250, 250, window=instructions_label)

    # create button to play audio
    play_btn = tk.Button(canvas, text="Play", bg="#3498DB", fg="#ffffff", font=("Helvetica", 16), padx=20, pady=10, command=play_audio)
    canvas.create_window(250, 400, window=play_btn)

# create main window
root = tk.Tk()
root.title("MindCare")
root.geometry("500x550")
root.resizable(False, False)
root.config(bg="#2C3E50")

# create canvas
canvas = tk.Canvas(root, width=500, height=550, bg="#2C3E50")
canvas.pack()

# create emoji buttons
happy_btn = tk.Button(canvas, text="😊", bg="#2C3E50", font=("Helvetica", 36), padx=20, pady=10, command=lambda: update_emotion("Happy"))
ok_btn = tk.Button(canvas, text="😐", bg="#2C3E50", font=("Helvetica", 36), padx=20, pady=10, command=lambda: update_emotion("Ok"))
sad_btn = tk.Button(canvas, text="😢", bg="#2C3E50", font=("Helvetica", 36), padx=20, pady=10, command=lambda: update_emotion("Sad"))

# create meditate button
meditate_btn = tk.Button(canvas, text="Meditate", bg="#3498DB", fg="#ffffff", font=("Helvetica", 16), padx=20, pady=10, command=open_meditate_window)

# create quote label
quote_label = tk.Label(canvas, text="", font=("Helvetica", 16), anchor="center", justify="center", wraplength=400, fg="#ffffff", bg="#2C3E50")

# add buttons and quote label to canvas
canvas.create_window(125, 250, window=happy_btn)
canvas.create_window(250, 250, window=ok_btn)
canvas.create_window(375, 250, window=sad_btn)
canvas.create_window(250, 400, window=meditate_btn)
canvas.create_window(250, 475, window=quote_label)

# run the GUI application
root.mainloop()
