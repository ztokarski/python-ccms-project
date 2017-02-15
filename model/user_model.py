import sqlite3
class User_model:
    conn = sqlite3.connect('ccms.db')
    users = conn.execute("SELECT * FROM users")
    for i in users:
        print(i)