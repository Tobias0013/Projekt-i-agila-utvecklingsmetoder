from tkinter import *
from sql_login import sql_login as database_con
import menu


class login_form:
    def __init__(self):
        """Constructor."""
        self.login_screen = Tk()
        self.ent_username = StringVar()
        self.ent_password = StringVar()
        self.lbl_message = StringVar()
        self.database = database_con()

    def start_login_form(self):
        """Constructs and start the form for login screen."""
        # Setting title of screen
        self.login_screen.title("Grundträning - ett redskap mot stress")
        # Setting height and width of screen
        self.login_screen.geometry("300x300")
        # Setting a function that executes when windows is closing
        self.login_screen.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Creating layout of login form
        Label(self.login_screen, width="300", text="Please enter details below", bg="cornflower blue",
              fg="white").pack()
        # Username Label
        Label(self.login_screen, text="Username * ").place(x=20, y=40)
        # Username textbox
        Entry(self.login_screen, textvariable=self.ent_username).place(x=90, y=42)
        # Password Label
        Label(self.login_screen, text="Password * ").place(x=20, y=80)
        # Password textbox
        Entry(self.login_screen, textvariable=self.ent_password, show="*").place(x=90, y=82)
        # Label for displaying login/register status
        Label(self.login_screen, text="", textvariable=self.lbl_message).place(x=95, y=100)

        # Buttons
        Button(self.login_screen, text="Login", width=10, height=1, bg="cornflower blue",
               command=self.btn_login).place(x=105, y=130)
        Button(self.login_screen, text="Register", width=10, height=1, bg="cornflower blue",
               command=self.btn_register).place(x=105, y=170)
        Button(self.login_screen, text="[skip]", width=10, height=1, bg="cornflower blue",
               command=self.skip).place(x=105, y=210)

        self.login_screen.mainloop()

    def btn_login(self):
        """Runs when pressing login button."""
        # Check if entry is empty
        if self.ent_username.get() == "" or self.ent_password.get() == "":
            self.lbl_message.set("fill all fields")
            return

        successful, account = self.database.login(self.ent_username.get(), self.ent_password.get())
        print(account[0])

        # Check if login successful
        if not successful:
            self.lbl_message.set("Wrong username or password")
            return

        self.lbl_message.set("Login successful")

        # close database connection
        self.database.close()
        # close the current window
        self.login_screen.destroy()
        # run menu.py
        menu.menu(account[0])

    def btn_register(self):
        """Runs when pressing register button."""
        # Check if entry is empty
        if self.ent_username.get() == "" or self.ent_password.get() == "":
            self.lbl_message.set("fill all fields")
            return

        # Checks if user already exists
        if self.database.user_exist(self.ent_username.get()):
            self.lbl_message.set("username already exists")
            return

        self.database.register(self.ent_username.get(), self.ent_password.get())
        self.lbl_message.set("register successful")

    def on_closing(self):
        """Runs when closing login window."""
        # Close database connection
        self.database.close()
        # Close the current window
        self.login_screen.destroy()

    def skip(self):
        """Run menu.py. [ta bort denna metod sen]"""
        # Close database connection
        self.database.close()
        # Close the current window
        self.login_screen.destroy()
        # Run menu.py
        menu.menu()
