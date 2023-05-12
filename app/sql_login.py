import hashlib

import sql


class sql_login(sql.sql):
    def __init__(self):
        super().__init__()

    def login(self, usr, pswd):
        """Execute login query to database. True = successful login, False = login failed"""
        # hash password
        pswd_hash = hashlib.sha256(pswd.encode()).hexdigest()

        # the reson for "(password=? OR password=?)" is to make application backward compatible
        query = "SELECT * FROM account WHERE username=? AND (password=? OR password=?)"
        self.cursor.execute(query, (usr, pswd_hash, pswd))

        res = self._get_result()
        if len(res) > 0:
            return True, res
        else:
            return False, None

    def register(self, usr, pswd):
        """Execute register query to database."""
        query = "INSERT INTO account(username, password) VALUES(?, ?)"
        self.cursor.execute(query, (usr, pswd))
        self.conn.commit()

    def user_exist(self, usr):
        """Checks if user already exists. True = user exists, False = user not exists."""
        query = "SELECT * FROM account WHERE username=?"
        self.cursor.execute(query, (usr,))

        res = self._get_result()

        if len(res) > 0:
            return True
        return False
