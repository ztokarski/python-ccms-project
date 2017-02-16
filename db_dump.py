from sqlite3 import OperationalError
import sqlite3
def clear_and_insert_db():
    conn = sqlite3.connect('ccms.db')
    c = conn.cursor()

    file = open('create_db.sql')
    sqlfile = file.read()
    file.close()

    commands = sqlfile.split(';')

    for line in commands:
        try:
            c.execute(line)
        except OperationalError as msg:
            print("Command skipped: ", msg, line)

clear_and_insert_db()