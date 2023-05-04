# Emotions and Quotes
This program is a simple Python script that demonstrates how to connect to a SQLite database using the sqlite3 module and retrieve a quote based on the user's input emotion.

# Getting Started
To run this script, you will need to have Python 3 installed on your computer. You will also need to have the sqlite3 module installed, which is included in the Python standard library.

To get started, clone or download the script and open it in your preferred Python IDE or text editor.


# Usage
- Instantiate an Emotions object by calling the Emotions() constructor. This will create a new database connection, create the emotions table (if it doesn't exist), and populate the table with some sample quotes for the emotions of "happy", "ok", and "sad".

- Prompt the user to enter an emotion by calling the input() function and passing in the string "Enter an emotion: ".

- Call the get_quote() method on the Emotions object and pass in the user's input as an argument. This will retrieve the quote for the given emotion from the emotions table in the database.

- Print the retrieved quote to the console.

- Close the database connection by calling the close_connection() method on the Emotions object.


# Contributing
If you have any suggestions or find any issues with the script, please feel free to open an issue or submit a pull request on GitHub.


# GUI


# Modern Login UI using Customtkinter and Emotion Tracker
This project contains two different user interfaces built with the help of the Customtkinter library and Emotion Tracker respectively.

# Custom Login UI using Customtkinter

The Custom Login UI uses Customtkinter library to create a modern and responsive login page.
It consists of two fields to input username and password, a login button, and a register button to create a new user account. 
After successful login or registration, a message dialog will be displayed with a success message. The project stores user account information in a file named "accounts.txt".

# Requirements
- Python 3.5 and above
- Customtkinter (Installation: pip install customtkinter)
- Pygame (Installation: pip install pygame)

# Emotion Tracker UI
The Emotion Tracker UI helps users to track their emotions and feelings. 
The UI displays three different emoji buttons: 😊, 😐, and 😢 to represent happy, ok, and sad emotions respectively. 
Users can click on the appropriate button to track their current emotion. Additionally, the UI provides a "Meditate" button to help users to calm down and relax their minds. 
The UI also displays a random motivational quote to inspire the users.

# Requirements
- Python 3.5 and above
- Pygame (Installation: pip install pygame)

# LOGIN

# Modern Login UI using Customtkinter
This is a simple Python program that demonstrates how to create a modern login system UI using the customtkinter library.
Requirements
- Python 3.5 or higher
- customtkinter library (installation guide can be found at https://pypi.org/project/customtkinter/)
- An existing accounts.txt file in the same directory as the program for storing user credentials.

# How to Use
- Clone or download the program files to your local machine.
- Install the customtkinter library by running pip install customtkinter on your terminal or command prompt.
- Run the program by executing python login_ui.py in your terminal or command prompt.
- The login system UI will open, and you can test its functionality by trying to log in with existing credentials or registering new ones.

# Program Details
The program utilizes customtkinter to create a modern login UI with a dark theme and blue color scheme. 
The UI has two entry fields for username and password, as well as a login and register button.
The register function opens a new window where users can register a new account by entering their desired username and password. 
The user's input is then saved to the accounts.txt file, and a registration successful message is displayed.
The login function reads the accounts.txt file to check if the entered username and password exist in the file.
If the credentials match, a login successful message is displayed, and the UI window is closed. 
If the username or password is incorrect, a corresponding warning message is displayed.
Upon successful login, the UI window is closed, and the program terminates.


# MUSIC PLAYER

This is a simple music player written in Python using the following libraries:

- tkinter for the GUI
- customtkinter for customizing the GUI appearance
- pygame for playing music
- PIL (Python Imaging Library) for image processing
- threading for running progress function in a separate thread

# Getting started
To run the program, you need to have Python installed on your system. You also need to have the above mentioned libraries installed. 
Once you have installed the libraries, save the code in a file with a .py extension and run the file. The music player window will appear on your screen.

# Usage
The music player window contains the following controls:

- Play/Pause button: to play or pause the current song
- Forward button: to skip to the next song
- Backward button: to go back to the previous song
- Volume slider: to adjust the volume of the music player
- Progress bar: to show the progress of the current song

To add more songs to the music player, simply add the file names of the songs and their album covers to the list_of_songs and list_of_covers arrays respectively.

# Customization
You can customize the appearance of the music player by changing the following lines of code:

- customtkinter.set_appearance_mode("System"): change the appearance mode of the music player. The available modes are "System" (default), "Light", and "Dark".
- customtkinter.set_default_color_theme("blue"): change the default color theme of the music player. The available themes are "blue" (default), "dark-blue", and "green".
