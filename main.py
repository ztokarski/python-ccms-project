import os
from ui import *
from open_list import *
from login import *
import sys

# def

def student_menu(name, surname):
    print("Hello, {}".format(name))
    print("")
    print(Ui.STUDENT_INTRO)
    option = input("Pick an option")

def main_menu():
    # while True:
    print(Ui.START_MAIN)
    user = Login().login_check()

    return user
# print(type(main()))
user = main_menu()
if isinstance(user, Student):
    student_menu(user.name, user.surname)
else:
    sys.exit()

main_menu()
# print(main())
# def menu_student()
# def student_menu():

# if __name__ == '__main__':
    # main()
