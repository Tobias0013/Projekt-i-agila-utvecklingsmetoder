import unittest
from unittest.mock import patch, call
import sys
import os
import tkinter as tk
import winsound

# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.grund_traning import grund_traning


class TestGrundTraining(unittest.TestCase):
    @patch("winsound.PlaySound")
    def test_grund_traning_command(self, mock_PlaySound):
        # Create the necessary test objects
        parent = tk.Tk()
        button = grund_traning(parent)
        
        # Simulate button click
        button.grund_traning_command()

        # Verify that PlaySound was called with the correct arguments
        expected_calls = [
            call("zero_to_ten_and_back.wav", winsound.SND_FILENAME),
            call("Count.wav", winsound.SND_FILENAME)
        ]
        mock_PlaySound.assert_has_calls(expected_calls)

if __name__ == "__main__":
    unittest.main()