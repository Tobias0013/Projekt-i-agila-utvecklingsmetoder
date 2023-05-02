import tkinter as tk
from tkinter import messagebox

from grund_traning import grund_traning
from calendar_form import calendar_form

class menu():
    def __init__(self, account):
        self.account = account
        self.menu()

    def menu(self):
        root = tk.Tk()
        root.title("Grundträning - ett redskap mot stress")

        label_frame = tk.Frame(root)
        label = tk.Label(root, text="Main menu", width= 22, font=("Arial", 24), bg="#3264a8")
        label.pack(side="top")

        button_frame = tk.Frame(root)
        button_frame.pack()

        # Create custom buttons for each button in the list
        button_list = []
        for i, value in enumerate(["Grundträning", "Fokusering", "Historik", "Kalender", "Exit"]):
            if value == "Grundträning":
                button = grund_traning(button_frame)  # GRUNDTRÄNINGSKLASSS
            else:
                button = tk.Button(button_frame, text=value, width= 50, height=2, padx=10, pady=10, bg="#3264a8", font=("Arial", 10))
            button.grid(row=i)
            button_list.append(button)

        # add event listener to kalender button
        button_list[3].config(command=self.btn_calender_pressed)
        # Allows quit button to exit
        button_list[-1].config(command=root.destroy)

        root.mainloop()

    def btn_calender_pressed(self):
        cal = calendar_form()
        cal.start_calender_form()
