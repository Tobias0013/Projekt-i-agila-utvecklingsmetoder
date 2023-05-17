import os
import sys
import unittest
sys.path.append("../app")
sys.path.append("app")
import sql_login

class MyTestCase(unittest.TestCase):
    def test_init_default_object(self):
        database = sql_login.sql_login()
        exp = sql_login.sql_login
        database.close()
        self.assertIsInstance(database, exp)

    def test_login(self):
        database = sql_login.sql_login()
        res, account = database.login("test", "test123")

        self.assertTrue(res)

        res, account = database.login("a", "a")

        database.close()
        self.assertFalse(res)

    def test_user_exist(self):
        database = sql_login.sql_login()
        res = database.user_exist("test")

        self.assertTrue(res)

        res = database.user_exist("a")

        database.close()
        self.assertFalse(res)

if __name__ == '__main__':
    unittest.main()
