import calendar
from tkinter import *
import random


class Calender:
    def __init__(self):
        self.root = Tk()
        self.root.title("Kalender")
        self.root.geometry("300x300")
        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)

    def start(self):
        # The "Display Date" button
        self.button = Button(self.root, text="Date", width=10,
                             height=1, bg="cornflower blue",
                             command=self.display_month).pack()
        # the Frame
        self.frame = Frame(self.root, background="black", width=100, height=5,
                           bg="cornflower blue").place(x=100, y=100)
        # Label inside the Frame
        self.label = Label(self.frame, text="Text", font=("Arial", 24),
                           fg="white", bg="black", width=10, height=2).pack()

        self.root.mainloop()

    def display_month(self):
        yy = random.choice([2000, 2010, 2013, 2023])
        mm = random.choice([1, 4, 5, 9])
        newtext = calendar.month(yy, mm)
        self.label.config(text=newtext)
