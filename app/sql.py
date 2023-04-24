import pyodbc


class sql:
    def __init__(self):
        self._DRIVER = "{ODBC Driver 17 for SQL Server}"
        self._SERVER = "LOCALHOST"
        self._DATABASE = "mediation_db"
        self.conn = None
        self.cursor = None

    def connect(self):
        """Connect to database."""
        conn_str = "DRIVER=" + self._DRIVER + "; " \
                   "SERVER=" + self._SERVER + "; " \
                   "DATABASE=" + self._DATABASE + "; " \
                   "Trusted_Connection=yes"
        self.conn = pyodbc.connect(conn_str)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_result(self):
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
