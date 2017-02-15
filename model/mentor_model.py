import sqlite3
import os

class Mentor_model:

    def __init__(self):
        self.conn = sqlite3.connect(os.path.realpath('../ccms.db'))
        self.db = self.conn.cursor()

    def get_mentors_list(self):
        mentors_list = self.db.execute("SELECT * FROM users where ID_role = 2")
        return mentors_list

    def add_mentor(self, *args):
        self.conn.execute("INSERT INTO `users`(`name`,`surname`,`login`, `ID_role`) VALUES ('{}','{}','{}', 2);".format(*args))
        self.conn.commit()


if __name__ == '__main__':
    model = Mentor_model()
    for i in model.get_mentors_list():
        print(i)

    model.add_mentor('Rubu', 'Bubu', 'rbb')

    for i in model.get_mentors_list():
        print(i)