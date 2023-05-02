import tkinter as tk
import winsound


class fokusering(tk.Button):  # Grundtraining class
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self["command"] = self.fokusering_command

    def fokusering_command(self):
        winsound.PlaySound("Fokusering.wav", winsound.SND_FILENAME)
        