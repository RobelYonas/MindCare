import unittest# Importing unittest module for unit testing
import sqlite3# Importing sqlite3 module for database operations
from Backend import Emotions# Importing Emotions class from Backend module


# Define a class to test the Emotions class

class TestEmotions(unittest.TestCase):

    # Create an instance of Emotions class before running the tests
    @classmethod
    def setUpClass(cls):
        cls.emotions = Emotions()

    # Test if the emotions table exists in the database
    def test_create_table(self):
        # Execute an SQL query to check if the emotions table exists in the database
        self.emotions.cursor.execute("""
            SELECT name FROM sqlite_master WHERE type='table' AND name='emotions'
        """)

        #  This line retrieves the first row of the query result, which should contain the quote string for the current emotion.
        result = self.emotions.cursor.fetchone()
        # Check if a result exists
        self.assertIsNotNone(result)

    # Test if quotes can be populated in the emotions table
    def test_populate_table(self):
        # Define a list of tuples containing emotions and quotes
        quotes = [
            ("happy", "Happiness is not something ready made. It comes from your own actions. - Dalai Lama"),
            ("ok", "It is better to be hated for what you are than to be loved for what you are not. - Andre Gide"),
            ("sad", "The best way to cheer yourself up is to try to cheer somebody else up. - Mark Twain")
        ]
        # Loop through the list of quotes and check if they can be retrieved from the database
        for emotion, quote in quotes:

            # Takes quote from database and checks for correlating emotion
            self.emotions.cursor.execute("""
                SELECT quote FROM emotions WHERE emotion=?
            """, (emotion,))
            result = self.emotions.cursor.fetchone()
            # Check if a result exists and if it matches the quote in the tuple
            self.assertIsNotNone(result)
            # Flags error if no matching quote to emotion
            self.assertEqual(result[0], quote)

    # Test if the Emotions class can retrieve quotes for different emotions
    def test_get_quote(self):
        # Check if the emotion given, gives us the correct corresponding quote
        happy_quote = self.emotions.get_quote("happy")
        self.assertEqual(happy_quote,
                         "Happiness is not something ready made. It comes from your own actions. - Dalai Lama")

        # Check if a message is returned for an invalid emotion
        invalid_emotion_quote = self.emotions.get_quote("angry")
        self.assertEqual(invalid_emotion_quote, "Sorry, I don't have a quote for that emotion.")

    # Close the database connection after all the tests have been run
    # If open, slows down laptop processing and puts database at risk
    @classmethod
    def tearDownClass(cls):
        cls.emotions.close_connection()


if __name__ == '__main__':
    unittest.main()