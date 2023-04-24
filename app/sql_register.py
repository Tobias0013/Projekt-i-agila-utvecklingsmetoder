import sql
import pyodbc


class sql_register(sql.sql):
    def __init__(self):
        super().__init__()

    def register_query(self, usr, pswd):
        """Execute register query to database."""
        query = "INSERT INTO login(username, password) VALUES('" + usr + "', '" + pswd + "')"
        self.cursor.execute(query)
        self.cursor.commit()

    def user_exist(self, usr):
        """Checks if user already exists. True = user exists, False = user not exists."""
        query = "SELECT * FROM login WHERE username='" + usr + "'"
        self.cursor.execute(query)

        res = self.get_result()

        if len(res) > 0:
            return True
        return False
