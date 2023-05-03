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


