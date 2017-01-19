import os
from ui import *
from open_list import *
from login import *
from user import *
import sys
import csv

# def

# def student_menu(name, surname):
#     print("Hello, {}".format(name))
#     print("")
#     print(Ui.STUDENT_INTRO)
#     option = input("Pick an option")
#     if option == "2":
#         print("{} {}".format(user.name, user.surname))
#         undone = Open().open_users("CSV/assignments.csv")
#         done = Open().open_users("CSV/sub_assignments.csv")
#         student_undone = undone
#         print("")
#         print("Done:")
#             # print(num, assignment[0].title(), assignment[1].title())
#         for submit in done:
#             if submit[0] == user.name.lower() + user.surname.lower():
#                 for x in student_undone:
#                     if submit[1] == x[0]:
#                         a = x
#                         student_undone.remove(a)
#                 print("{} Grade: {} Date {}.".format(submit[1].title(), submit[2], submit[3]))
#             else:
#                 continue
#         print("Undone:")
#         for num, dupa in enumerate(student_undone, 1):
#             print("{}. {} - {}".format(num, dupa[0].title(), dupa[1]))
#
#         arg = ""
#         which_to_submit = input("Which position on the list would You like to submit?")
#
#         for num, dupa in enumerate(student_undone, 1):
#             if which_to_submit == str(num):
#                 arg = str(dupa[0])
#             else:
#                 raise ValueError
#         student = Student(name, surname)
#         submitted_assigment = student.submit_assigment(arg)
#         done.append(submitted_assigment)
#         with open("CSV/sub_assignments.csv", "w") as f:
#             writer = csv.writer(f)
#             writer.writerows(done)




# def main_menu():
#     # while True:
#     print(Ui.START_MAIN)
#     user = Login().login_check()
#
#     return user
# # print(type(main()))
# user = main_menu()
# if isinstance(user, Student):
#     student_menu(user.name, user.surname)
# else:
#     sys.exit()
#
# main_menu()
# print(main())
# def menu_student()
# def student_menu():
def main():
    print(Ui.START_MAIN)
    Menu.login_and_menu()
if __name__ == '__main__':
    main()
