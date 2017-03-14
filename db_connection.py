import sqlite3
import os

class DB:

    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, "ccms.db")

    @classmethod
    def get_connection(cls):
        base = sqlite3.connect(cls.filename)
        return base

    @classmethod
    def close_connection(cls):
        return cls.close()
