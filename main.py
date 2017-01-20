import os
from ui import *
from open_lists import *
from login import *
from user import *
import sys
import csv


def main():
    Menu.login_and_menu()

# object_list = StudentList().get_students_list()
# object_list2 = MentorList().get_mentors_list()
# # object_list3 = AssignmentList().get_assignment_list()
#
#     # while True:
#     #     print(Ui.START_MAIN)
#         # Login().login_check()
#     print(Display().print_table(object_list))
#     print(Display().print_table(object_list2))
    # print(object_list)

if __name__ == '__main__':
    main()
