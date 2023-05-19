import winsound
import unittest
from unittest.mock import patch
import sys
import os
# Add the path to the 'app' module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.fokusering import fokusering


class TestFokusering(unittest.TestCase):
    def setUp(self):
        self.fokusering_btn = fokusering(None)

    @patch('winsound.PlaySound')
    def test_play_sounds(self, mock_play_sound):
        self.fokusering_btn.play_sounds()
        mock_play_sound.assert_called_once_with("Fokusering.wav", winsound.SND_FILENAME)

if __name__ == '__main__':
    unittest.main()
