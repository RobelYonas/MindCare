import tkinter
import customtkinter
import pygame
from PIL import Image, ImageTk
from threading import *
import time
# import math

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

width = 500
height = 500
root = customtkinter.CTk()
root.title('Music Player')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

root.geometry("%dx%d+%d+%d" % (width, height, x, y))

pygame.mixer.init()

list_of_songs = ['Audio-1.mp3', 'Audio-2.mp3']
list_of_covers = ['med-1.jpg', 'med-2.jpg']
n = 0
paused = False

def get_album_cover(song_name, n):
    image1 = Image.open(list_of_covers[n])
    image2=image1.resize((250, 250))
    load = ImageTk.PhotoImage(image2)
    label1 = tkinter.Label(root, image=load)
    label1.image = load
    label1.place(relx=.25, rely=.06)
    label1.place(relx=.265, rely=.06)
    stripped_string = song_name[6:-4]
    song_name_label = tkinter.Label(text = stripped_string, bg='#222222', fg='white')
    song_name_label.place(relx=.49, rely=.6)

    global time_label
    time_label = tkinter.Label(root, text='00:00', font=('Helvetica', 12), bg='#222222', fg='white')
    time_label.place(relx=0.5, rely=0.98, anchor='center')


def play_music(duration=0):
    global n
    global paused
    if pygame.mixer.music.get_busy() and not paused:
        pygame.mixer.music.pause()
        paused = True
        play_button.configure(text="▶️")
    else:
        threading(duration)
        current_song = n
        song_name = list_of_songs[n]
        pygame.mixer.music.load(song_name)
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.set_volume(.5)
        get_album_cover(song_name, n)

        play_button.configure(text="⏸️")
        paused = False  # Reset the 'paused' variable to False


def threading(duration=0):
    t1 = Thread(target=progress, args=(duration,))
    t1.start()


def progress(duration):
    a = pygame.mixer.Sound(f'{list_of_songs[n]}')
    if duration != 0:
        song_len = duration
    else:
        song_len = a.get_length() * 3
    while pygame.mixer.music.get_busy():
        time.sleep(.1)
        current_pos = pygame.mixer.music.get_pos() / 1000  # Get current position of the song in milliseconds
        progressbar.set(current_pos / song_len)  # Update progressbar
        minutes = int(current_pos // 60)  # Calculate the number of minutes
        seconds = int(current_pos % 60)  # Calculate the number of seconds
        time_str = f"{minutes:02d}:{seconds:02d}"  # Format the time as mm:ss
        time_label.config(text=time_str)  # Update the time label

        # Check if the progress has reached the end of the song
        if current_pos >= song_len:
            pygame.mixer.music.stop()
            break



def button_clicked(duration):
    play_music(duration)


def skip_forward():
    global n
    n += 1
    if n >= len(list_of_songs):
        n = 0
    pygame.mixer.music.stop()
    play_music()


def skip_back():
    global n
    n -= 1
    if n < 0:
        n = len(list_of_songs) - 1
    pygame.mixer.music.stop()
    play_music()


def volume(value):
    #print(value)
    pygame.mixer.music.set_volume(value)

# Buttons
play_button = customtkinter.CTkButton(master=root, text='⏯️', command=play_music)
play_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

skip_f = customtkinter.CTkButton(master=root, text='>', command=skip_forward, width=2)
skip_f.place(relx=0.7, rely=0.7, anchor=tkinter.CENTER)

skip_b = customtkinter.CTkButton(master=root, text='<', command=skip_back, width=2)
skip_b.place(relx=0.3, rely=0.7, anchor=tkinter.CENTER)

slider = customtkinter.CTkSlider(master=root, from_= 0, to=1, command=volume, width=210)
slider.place(relx=0.5, rely=0.78, anchor=tkinter.CENTER)

progressbar = customtkinter.CTkProgressBar(master=root, progress_color='#32a85a', width=250)
progressbar.place(relx=.5, rely=.85, anchor=tkinter.CENTER)

button1 = customtkinter.CTkButton(master=root, text='30 sec', command=lambda: button_clicked(30))
button1.place(relx=0.2, rely=0.9, anchor=tkinter.CENTER)

button2 = customtkinter.CTkButton(master=root, text='45 sec', command=lambda: button_clicked(45))
button2.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

button3 = customtkinter.CTkButton(master=root, text='1 min', command=lambda: button_clicked(60))
button3.place(relx=0.8, rely=0.9, anchor=tkinter.CENTER)



def run():
    root.mainloop()

