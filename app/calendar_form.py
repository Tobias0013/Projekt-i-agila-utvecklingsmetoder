from tkinter import *
from tkcalendar import *
from sql_emotion import sql_emotion as database_con
from datetime import date

class calendar_form:
    def __init__(self, account):
        """Constructor."""
        self.calendar_form = Tk()
        self.database = database_con()
        self.account = account

        # Setting title of screen
        self.calendar_form.title("Grundträning - ett redskap mot stress")
        # Setting height and width of screen
        self.calendar_form.geometry("300x350")
        # Setting a function that executes when windows is closing
        self.calendar_form.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Calendar, set current date
        today = date.today()
        self.calendar = Calendar(self.calendar_form, selectmode='day', year=today.year, month=today.month, day=today.day)
        self.calendar.pack(pady=10)
        # Button get date
        self.btn_get_date = Button(self.calendar_form, text="[Hämta]", width=10, height=1, bg="cornflower blue", command=self.click)
        self.btn_get_date.pack(pady=10)
        # Label date
        self.lbl_date = Label(self.calendar_form, text="")
        self.lbl_date.pack(pady=10)

        self.load_emotion()

        self.calendar_form.mainloop()

    def load_emotion(self):
        res = self.database.select_emotion(self.account.get("username"))
        # print(res) # DEBUG

        for r in res:
            dt = r.get("emotion_date")
            rating = "Rating: " + str(r.get("emotion_rating"))
            text = " Text: " + r.get("emotion_text")

            self.calendar.calevent_create(date=dt, text=rating + text, tags="Message")
            self.calendar.tag_config("Message", background="#90ee90", foreground="black")

    def click(self):
        """Fetch events from selected date"""
        self.lbl_date.config(text="Selected Date is: " + self.calendar.get_date())

        dt_arr = self.calendar.get_date().split('/')
        dt = date(int("20" + dt_arr[2]), int(dt_arr[0]), int(dt_arr[1]))

        # Go through all events and make new label per event for selected date
        for value, _ in enumerate(self.calendar.calevents):
            val = self.calendar.calevents[_]
            if val['date'] == dt:
                Label(self.calendar_form, text=(f"{val['date']}, {val['text']}, {val['tags'][0]}")
                      .replace('\n', '') + '\n').pack()

    def on_closing(self):
        """Runs when closing login window."""
        # Close database connection
        self.database.close()
        # Close the current window
        self.calendar_form.destroy()
