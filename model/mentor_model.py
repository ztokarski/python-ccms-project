import sqlite3
import control\students


class Student_model:
    conn = sqlite3.connect('ccms.db')

    mentor_db = conn.execute("SELECT * FROM users WHERE id_role = 2")

    return mentor_db_db