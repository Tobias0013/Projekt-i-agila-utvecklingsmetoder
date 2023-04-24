import sql
import pyodbc


class sql_login(sql.sql):
    def __init__(self):
        super().__init__()

    def login_query(self, usr, pswd):
        """Execute login query to database."""
        query = "SELECT * FROM login WHERE username='" + usr + "' AND password='" + pswd + "'"
        self.cursor.execute(query)
