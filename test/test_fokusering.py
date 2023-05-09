import unittest
from unittest.mock import patch, call
import sys
import os
import tkinter as tk
import winsound
# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fokusering import fokusering


class Test_fokusering(unittest.TestCase):
    @patch("winsound.PlaySound")
    def test_fokusering_command(self, mock_PlaySound):
        # Create the necessary test objects
        parent = tk.Tk()
        button = fokusering(parent)
        # Simulate button click
        button.fokusering_command()
        # Verify that PlaySound was called with the correct arguments
        expected_calls = [
            call("Fokusering.wav", winsound.SND_FILENAME),
        ]
        mock_PlaySound.assert_has_calls(expected_calls)


if __name__ == "__main__":
    unittest.main()
