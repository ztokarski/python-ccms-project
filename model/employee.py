import sqlite3
import control\students


class Employee_model:
    conn = sqlite3.connect('ccms.db')

    employee_db = conn.execute("SELECT * FROM users WHERE id_role = 3")

    return employee_db