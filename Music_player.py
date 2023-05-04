# Import necessary libraries
import tkinter
import customtkinter
import pygame
from PIL import Image, ImageTk
from threading import *
import time

# Set appearance mode and default color theme
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# Set window dimensions and title
width = 500
height = 500
root = customtkinter.CTk()
root.title('Music Player')

# Get screen dimensions and center window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))

# Initialize mixer and create list of songs and album covers
pygame.mixer.init()
list_of_songs = ['Audio-1.mp3', 'Audio-2.mp3']
list_of_covers = ['med-1.jpg', 'med-2.jpg']

# Initialize variables
n = 0
paused = False

# Function to get album cover image
def get_album_cover(song_name, n):
    image1 = Image.open(list_of_covers[n])
    image2=image1.resize((250, 250))
    load = ImageTk.PhotoImage(image2)
    label1 = tkinter.Label(root, image=load)
    label1.image = load
    label1.place(relx=.28, rely=.06)

    stripped_string = song_name[6:-4]
    song_name_label = tkinter.Label(text = stripped_string, bg='#222222', fg='white')
    song_name_label.place(relx=.49, rely=.6)

    global time_label
    time_label = tkinter.Label(root, text='00:00', font=('Helvetica', 12))
    time_label.place(relx=0.5, rely=0.92, anchor='center')

# Function to update progress of current song
def progress():
    a = pygame.mixer.Sound(f'{list_of_songs[n]}')
    song_len = a.get_length() * 3
    while pygame.mixer.music.get_busy():
        time.sleep(.1)
        current_pos = pygame.mixer.music.get_pos() / 1000  # Get current position of the song in milliseconds
        progressbar.set(current_pos / song_len)  # Update progressbar
        minutes = int(current_pos // 60)  # Calculate the number of minutes
        seconds = int(current_pos % 60)  # Calculate the number of seconds
        time_str = f"{minutes:02d}:{seconds:02d}"  # Format the time as mm:ss
        time_label.config(text=time_str)  # Update the time label

# Function to run progress function in a separate thread
def threading():
    t1 = Thread(target=progress)
    t1.start()

# Function to play or pause music
def play_music():
    global n
    global paused
    if pygame.mixer.music.get_busy() and not paused:
        pygame.mixer.music.pause()
        paused = True
        play_button.configure(text="▶️")
    else:
        threading()
        current_song = n
        song_name = list_of_songs[n]
        pygame.mixer.music.load(song_name)
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.set_volume(.5)
        get_album_cover(song_name, n)

        play_button.configure(text="⏸️")
        paused = False  # Reset the 'paused



def skip_forward():
    global n # access the global variable n
    n += 1 # increment n by 1 to go to the next song in the list
    if n >= len(list_of_songs):# if n exceeds the number of songs in the list
        n = 0 # reset n to 0 to start from the beginning of the list
    pygame.mixer.music.stop()# stop the currently playing song
    play_music() # play the next song in the list


def skip_back():
    global n # access the global variable n
    n -= 1 #decrement n by 1 to go to the previous song in the list
    if n < 0: # if n becomes negative
        n = len(list_of_songs) - 1# set n to the index of the last song in the list
    pygame.mixer.music.stop()# stop the currently playing song
    play_music()# play the previous song in the list


def volume(value):
    #print(value)
    pygame.mixer.music.set_volume(value) # set the volume of the music player to the slider


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

def run():
    root.mainloop()

run()

