import mariadb


class sql:
    def __init__(self):
        try:
            self.conn = mariadb.connect(
                user="meditation_user",
                password="J%xLsAb19475",
                host="83.250.124.8",
                port=3306,
                database="mediation_db"
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def _get_result(self):
        """Gets result data from SELECT statement in form of list of dicts."""
        # takes out column names
        column_name = []
        for col_name in self.cursor.description:
            column_name.append(col_name[0])

        # creates list of dict for every row
        res = []
        for row in self.cursor.fetchall():
            res.append(dict(zip(column_name, row)))

        return res
