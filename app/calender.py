from tkinter import *
import calendar


class Calender:
    def __init__(self):
        """Construct window."""
        self.root = Tk()
        self.root.title("Kalender")
        self.root.geometry("300x300")
        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)

        # Set year and month variables
        self.yy = ""
        self.mm = ""

        # Start window
        self.start()

    def start(self):
        """Start Calendar window with widgets."""
        # Button for confirming entry
        Label(self.root, text="Skriv in år och månad att visa").pack()
        Button(self.root, width=8, height=2,
               text="Enter", bg="cornflower blue",
               command=self.check_date).place(x=220, y=38)

        # Year label and entry
        Label(self.root, text='År').place(x=30, y=40)
        Entry(self.root, textvariable=self.yy).place(x=90, y=42)

        # Month label and entry
        Label(self.root, text='Månad').place(x=30, y=80)
        Entry(self.root, textvariable=self.mm).place(x=90, y=82)
        self.label = Label(self.root, width=100)
        self.label.pack()

        # Start window
        self.root.mainloop()

    def check_date(self):
        """Display year and month."""
        # While year/month entries are not filled
        validation = ["", 0]
        c1 = self.yy in validation
        c2 = self.mm in validation
        if c1 or c2:
            self.label.config(text="fill all fields",
                              font=("", 12),)
            return
        else:
            # Display specified month
            cal = calendar.month(self.yy, self.mm)
            self.label.config(text=cal, font=("", 18))
