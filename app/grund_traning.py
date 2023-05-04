import tkinter as tk
import threading
import winsound


class grund_traning(tk.Button):  # Grundtraining class
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self["command"] = self.grund_traning_command

    def grund_traning_command(self):
        sound_thread = threading.Thread(target=self.play_sounds)
        sound_thread.start()

    def play_sounds(self):
        winsound.PlaySound("zero_to_ten_and_back.wav", winsound.SND_FILENAME)
        winsound.PlaySound("Count.wav", winsound.SND_FILENAME)