import os
import sys
import unittest
sys.path.append("../app")
sys.path.append("app")
import sql
class Test_sql(unittest.TestCase):
    def test_init_default_object(self):
        """Instantiate an object and check its properties.
        Also test connection."""
        database = sql.sql()
        exp = sql.sql
        database.close()
        self.assertIsInstance(database, exp)

if __name__ == '__main__':
    unittest.main()
