import sqlite3


class DatabaseConnector():
    def __init__(self):
        self.con = sqlite3.connect("tutorial.db")
        self.cur = self.con.cursor()

    def select_table(self, table_name):
        res = self.cur.execute(f"SELECT * FROM {table_name}")
        return res
