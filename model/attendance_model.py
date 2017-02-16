import sqlite3


class AttendanceModel:  # tworzyc instacncje z danymi
    attendance_list = []

    def __init__(self):
        self.con = sqlite3.connect('ccms.db')
        self.db = self.con.cursor()

    def get_attendance_from_db(self):
        self.db.execute("SELECT * FROM attendance")
        return self.db.fetchall()

    def set_attendance(self):
        pass
