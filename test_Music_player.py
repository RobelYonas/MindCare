import unittest
import Music_player

class TestMusicPlayer(unittest.TestCase):

    def test_play_music(self):
        Music_player.play_music()
        self.assertTrue(Music_player.paused == False)

    def test_initial_state(self):
        assert Music_player.n == 0
        assert Music_player.paused == False
        assert Music_player.list_of_songs == ['Audio-1.mp3', 'Audio-2.mp3']
        assert Music_player.list_of_covers == ['med-1.jpg', 'med-2.jpg']

    def test_get_album_cover(self):
        Music_player.get_album_cover('Audio-1.mp3', 0)
        self.assertTrue(Music_player.n == 0)
        self.assertTrue(Music_player.paused == False)
        self.assertTrue(Music_player.list_of_songs == ['Audio-1.mp3', 'Audio-2.mp3'])
        self.assertTrue(Music_player.list_of_covers == ['med-1.jpg', 'med-2.jpg'])

    def test_skip_back(self):
        # Set the current song to the second song in the list
        Music_player.n = 1

        # Call the skip_back function
        Music_player.skip_back()

        # Check that the current song is now the first song in the list
        assert Music_player.n == 0

    def test_skip_forward(self):
        # Set the current song to the first song in the list
        Music_player.n = 0

        # Call the skip_forward function
        Music_player.skip_forward()

        # Check that the current song is now the second song in the list
        assert Music_player.n == 1

    def test_threading(self):
        Music_player.threading()
        self.assertTrue(Music_player.paused == False)


    def test_volume(self):
        Music_player.volume(0.5)
        self.assertTrue(Music_player.paused == False)





if __name__ == '__main__':
    unittest.main()
