import sqlite3


class Emotions:
    def __init__(self):
        self.connection = sqlite3.connect('mydata.db')
        self.cursor = self.connection.cursor()
        self.create_table()
        self.populate_table()

    def create_table(self):
        # create the emotions table if it doesn't exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS emotions (
                emotion TEXT,
                quote TEXT
            );
        """)

    def populate_table(self):
        # insert some quotes for the different emotions
        self.cursor.execute("""
            INSERT INTO emotions VALUES
                ('happy', 'Happiness is not something ready made. It comes from your own actions. - Dalai Lama'),
                ('ok', 'It is better to be hated for what you are than to be loved for what you are not. - Andre Gide'),
                ('sad', 'The best way to cheer yourself up is to try to cheer somebody else up. - Mark Twain');
        """)

    def get_quote(self, emotion):
        # select the quote for the given emotion
        self.cursor.execute("""
            SELECT quote FROM emotions
            WHERE emotion = ?
        """, (emotion,))

        # fetch the quote and return it
        result = self.cursor.fetchone()
        if result is None:
            return "Sorry, I don't have a quote for that emotion."
        else:
            return result[0]

    def close_connection(self):
        # commit the changes to the database and close the connection
        self.connection.commit()
        self.connection.close()


# example usage
emotions = Emotions()

# prompt the user to enter an emotion
"""emotion = input("Enter an emotion: ")

# retrieve the quote for the given emotion and print it out
quote = emotions.get_quote(emotions)
print(quote)

# close the connection to the database"""
emotions.close_connection()
