import tkinter
import customtkinter
import pygame
from PIL import Image, ImageTk
from threading import *
import time


class MusicPlayer:
    def __init__(self):
        customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        self.root = customtkinter.CTk()
        self.root.title('Music Player')
        self.root.geometry('400x500')
        pygame.mixer.init()

        self.list_of_songs = ['Audio-1.mp3', 'Audio-2.mp3']
        self.list_of_covers = ['med-1.jpg', 'med-2.jpg']
        self.n = 0
        self.paused = False

        self.play_button = None
        self.skip_f = None
        self.skip_b = None
        self.slider = None
        self.progressbar = None
        self.time_label = None

        self.create_widgets()

    def create_widgets(self):
        self.get_album_cover(self.list_of_songs[self.n], self.n)

        # Buttons
        self.play_button = customtkinter.CTkButton(master=self.root, text='⏯️', command=self.play_music)
        self.play_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

        self.skip_f = customtkinter.CTkButton(master=self.root, text='>', command=self.skip_forward, width=2)
        self.skip_f.place(relx=0.7, rely=0.7, anchor=tkinter.CENTER)

        self.skip_b = customtkinter.CTkButton(master=self.root, text='<', command=self.skip_back, width=2)
        self.skip_b.place(relx=0.3, rely=0.7, anchor=tkinter.CENTER)

        self.slider = customtkinter.CTkSlider(master=self.root, from_=0, to=1, command=self.volume, width=210)
        self.slider.place(relx=0.5, rely=0.78, anchor=tkinter.CENTER)

        self.progressbar = customtkinter.CTkProgressBar(master=self.root, progress_color='#32a85a', width=250)
        self.progressbar.place(relx=.5, rely=.85, anchor=tkinter.CENTER)

    def get_album_cover(self, song_name, n):
        image1 = Image.open(self.list_of_covers[n])
        image2 = image1.resize((250, 250))
        load = ImageTk.PhotoImage(image2)
        label1 = tkinter.Label(self.root, image=load)
        label1.image = load
        label1.place(relx=.19, rely=.06)

        stripped_string = song_name[6:-4]
        song_name_label = tkinter.Label(text=stripped_string, bg='#222222', fg='white')
        song_name_label.place(relx=.4, rely=.6)

        self.time_label = tkinter.Label(self.root, text='00:00', font=('Helvetica', 12))
        self.time_label.place(relx=0.5, rely=0.92, anchor='center')

    def progress(self):
        a = pygame.mixer.Sound(f'{self.list_of_songs[self.n]}')
        song_len = a.get_length() * 3
        while pygame.mixer.music.get_busy():
            time.sleep(.1)
            current_pos = pygame.mixer.music.get_pos() / 1000  # Get current position of the song in milliseconds
            self.progressbar['value'] = current_pos / song_len * 100
