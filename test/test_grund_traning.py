import unittest
from unittest.mock import patch
import sys
import os
import winsound
import tkinter as tk

# Add the path to the 'app' module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.grund_traning import grund_traning


class TestGrundTraning(unittest.TestCase):
    def setUp(self):
        self.grund_traning_btn = grund_traning(None)

    @patch('winsound.PlaySound')
    def test_play_sounds(self, mock_play_sound):
        self.grund_traning_btn.play_sounds()

        expected_calls = [
            ("zero_to_ten_and_back.wav", winsound.SND_FILENAME),
            ("Count.wav", winsound.SND_FILENAME)
        ]
        actual_calls = [call[0] for call in mock_play_sound.call_args_list]

        self.assertEqual(actual_calls, expected_calls)

if __name__ == '__main__':
    unittest.main()
