import sql


class sql_emotion(sql.sql):
    def __init__(self):
        super().__init__()

    def insert_emotion(self, rating, text, date, usr):
        query = "INSERT INTO emotion(emotion_rating, emotion_text, emotion_date, account_account_username)" \
                 " VALUES(?, ?, ?, ?)"
        self.cursor.execute(query, (rating, text, date, usr))
        self.conn.commit()

    def select_emotion(self, usr):
        query = "SELECT emotion_rating, emotion_text, emotion_date " \
                "FROM account, emotion " \
                "WHERE username=emotion.account_account_username " \
                "AND username=?"
        self.cursor.execute(query, (usr,))

        return self._get_result()

    def insert_meditation(self, date, usr):
        query = "INSERT INTO meditation(meditation_date, account_account_username) " \
                "VALUES(?, ?)"
        self.cursor.execute(query, (date, usr))
        self.conn.commit()

    def select_meditation(self, usr):
        query = "SELECT meditation_date " \
                "FROM account, meditation " \
                "WHERE username=account_account_username " \
                "AND username=?"
        self.cursor.execute(query, (usr,))

        return self._get_result()