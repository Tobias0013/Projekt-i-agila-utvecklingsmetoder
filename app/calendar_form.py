from tkinter import *
from sql_login import sql_login as database_con
import menu
from tkcalendar import Calendar
from datetime import date


class calendar_form:
    def __init__(self):
        """Constructor."""
        self.calendar_form = Tk()
        # self.ent_username = StringVar()
        # self.ent_password = StringVar()
        # self.lbl_message = StringVar()
        # self.database = database_con()

        # Setting title of screen
        self.calendar_form.title("Grundträning - ett redskap mot stress")
        # Setting height and width of screen
        self.calendar_form.geometry("300x300")
        # Setting a function that executes when windows is closing
        self.calendar_form.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Calendar, set current date
        today = date.today()
        self.calendar = Calendar(self.calendar_form, selectmode='day', year=today.year, month=today.month, day=today.day)
        self.calendar.pack(pady=10)
        # Button get date
        self.btn_get_date = Button(self.calendar_form, text="Get Date", width=10, height=1, bg="cornflower blue", command=self.click)
        self.btn_get_date.pack(pady=10)
        # Label date
        self.lbl_date = Label(self.calendar_form, text="")
        self.lbl_date.pack(pady=10)

        self.calendar_form.mainloop()

    def click(self):
        self.lbl_date.config(text="Selected Date is: " + self.calendar.get_date())

    def on_closing(self):
        """Runs when closing login window."""
        # Close database connection
        # self.database.close()
        # Close the current window
        self.calendar_form.destroy()
