import tkinter as tk
import winsound
import threading


class fokusering(tk.Button):  # Fokusering class
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self["command"] = self.fokusering_command

    def fokusering_command(self):
        sound_thread = threading.Thread(target=self.play_sounds)
        sound_thread.start()

    def play_sounds(self):
        winsound.PlaySound("Fokusering.wav", winsound.SND_FILENAME)