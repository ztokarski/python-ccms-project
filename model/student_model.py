import sqlite3
# import control\students

class Student_model:
    
    conn = sqlite3.connect('ccms.db')

    students_db = conn.execute("SELECT * FROM users WHERE id_role = 1")

    # return students_db