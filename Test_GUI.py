import unittest
import os

from Music_player import MusicPlayer
from Backend import Emotions
from main import LoginUI, GUI


class TestLoginUI(unittest.TestCase):

    def setUp(self):
        self.ui = LoginUI()

    def test_save(self):
        # create new user and save credentials
        self.ui.register_user_entry.insert(0, "new_user")
        self.ui.register_pass_entry.insert(0, "password")
        self.ui.save()

        # check if the file was created and contains the new user credentials
        self.assertTrue(os.path.isfile("accounts.txt"))
        with open('accounts.txt', 'r') as f:
            data = f.readlines()
        self.assertIn("new_user,password\n", data)

    def test_login_success(self):
        # create a dummy user and add credentials to accounts file
        with open('accounts.txt', 'a') as f:
            f.write("dummy_user,password\n")

        # log in with dummy user credentials
        self.ui.user_entry.insert(0, "dummy_user")
        self.ui.pass_entry.insert(0, "password")
        self.ui.login()

        # check if login message box was displayed
        self.assertEqual(self.ui.app.state(), "withdrawn")

    def test_login_wrong_password(self):
        # create a dummy user and add credentials to accounts file
        with open('accounts.txt', 'a') as f:
            f.write("dummy_user,password\n")

        # log in with dummy user credentials and wrong password
        self.ui.user_entry.insert(0, "dummy_user")
        self.ui.pass_entry.insert(0, "wrong_password")
        self.ui.login()

        # check if warning message box was displayed
        self.assertIn("Please check your password", self.ui.app.children['!warning'].cget("message"))

    def test_login_user_not_found(self):
        # log in with non-existing user credentials
        self.ui.user_entry.insert(0, "non_existing_user")
        self.ui.pass_entry.insert(0, "password")
        self.ui.login()

        # check if error message box was displayed
        self.assertIn("Please check your username", self.ui.app.children['!error'].cget("message"))

    def tearDown(self):
        # delete accounts file after each test
        if os.path.isfile("accounts.txt"):
            os.remove("accounts.txt")


class TestGUI(unittest.TestCase):

    def setUp(self):
        self.gui = GUI()

    def test_update_emotion(self):
        # test if emotion changes when button is clicked
        self.assertEqual(self.gui.emotions.current_emotion, None)
        self.gui.happy_btn.invoke()
        self.assertEqual(self.gui.emotions.current_emotion, "Happy")
        self.gui.ok_btn.invoke()
        self.assertEqual(self.gui.emotions.current_emotion, "Ok")
        self.gui.sad_btn.invoke()
        self.assertEqual(self.gui.emotions.current_emotion, "Sad")

    def test_open_meditate_window(self):
        # test if meditate window opens when button is clicked
        self.gui.meditate_btn.invoke()
        self.assertIsInstance(self.gui.music_player, MusicPlayer)

    def tearDown(self):
        self.gui.root.destroy()


if __name__ == "__main__":
    unittest.main()
