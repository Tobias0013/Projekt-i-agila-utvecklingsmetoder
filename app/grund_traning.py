import tkinter as tk
import winsound


class grund_traning_button(tk.Button):  # Grundtraining class
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.config(width=50, height=2, padx=10, pady=10, bg="#3264a8", font=("Arial", 10))
        self["text"] = "Grundträning"
        self["command"] = self.grund_traning_command

    def grund_traning_command(self):
        winsound.PlaySound("zero_to_ten_and_back.wav", winsound.SND_FILENAME)
        winsound.PlaySound("Count.wav", winsound.SND_FILENAME)