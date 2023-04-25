import sql


class sql_login(sql.sql):
    def __init__(self):
        super().__init__()

    def login(self, usr, pswd):
        """Execute login query to database. True = successful login, False = login failed"""
        query = "SELECT * FROM account WHERE username='" + usr + "' AND password='" + pswd + "'"
        self.cursor.execute(query)

        res = self._get_result()
        if len(res) > 0:
            return True
        else:
            return False

    def register(self, usr, pswd):
        """Execute register query to database."""
        query = "INSERT INTO account(username, password) VALUES(?, ?)"
        self.cursor.execute(query, (usr, pswd))
        self.conn.commit()

    def user_exist(self, usr):
        """Checks if user already exists. True = user exists, False = user not exists."""
        query = "SELECT * FROM account WHERE username='" + usr + "'"
        self.cursor.execute(query)

        res = self._get_result()

        if len(res) > 0:
            return True
        return False
