import sqlite3
import os

class Student_model:
    
    def __init__(self):
        self.conn = sqlite3.connect(os.path.realpath('../ccms.db'))
        self.db = self.conn.cursor()

    def get_students_list(self):
        students_list = self.db.execute("SELECT * FROM users where ID_role = 1")
        return students_list

    def add_student(self, *args):
        self.conn.execute("INSERT INTO `users`(`name`,`surname`,`login`) VALUES ('{}','{}','{}');".format(*args))
        self.conn.commit()

if __name__ == '__main__':
    model = Student_model()
    for i in model.get_students_list():
        print(i)

    model.add_student('Stude', "Studencik" ,'ss')

    for i in model.get_students_list():
        print(i)