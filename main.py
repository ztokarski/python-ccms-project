
from view.login_view import *

def main():
    Login_view.login_password()

# import os
# from login import *
# from user import *
import sys
import csv
from model.attendance_model import AttendanceModel
from control.attendance import AttendanceControl
from tabulate import tabulate


# def main():
#     # Menu.login_and_menu()
#
#     # view attendance
#     a = AttendanceModel()
#     attendance_list = a.get_attendance_from_db()  # cr8 list of list
#     headers = ["id", "data", "attendance", "id_student"]
#     print(tabulate((AttendanceControl.display_attendance(a.get_attendance_from_db())), headers, tablefmt="fancy_grid",numalign="center"))
#     AttendanceControl.add_attendance(attendance_list, 8, 1)
#     print(tabulate((AttendanceControl.display_attendance(a.get_attendance_from_db())), headers, tablefmt="fancy_grid",numalign="center"))
#
# >>>>>>> 0e4195a45b92fed5f5954140ceabc6d1b14cf934

if __name__ == '__main__':
    main()
