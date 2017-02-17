from view.employee_view import EmployeeUI
from control.mentors import MentorControl
from model.mentor_model import *
from tabulate import tabulate

class ManagerUI(EmployeeUI):
    def __init__(self, manager):
        super().__init__(manager)

    @classmethod
    def show_manager_menu(cls):
        while True:
            print(
                "\n/-----------------------------------------------------"
                "\n| Manager menu:"
                "\n| (1) Show Mentors list."
                "\n| (2) Add new Mentor."
                "\n| (3) Remove Mentor."
                "\n| (4) Show students list."
                "\n| (5) Show Employees list."
                "\n| (6) Show students average grade"
                "\n| (7) Show full statistics about mentors and students"
                "\n| (0) Exit"
                "\n\-----------------------------------------------------"
            )
            user_choose = input('Your choose: ')
            if user_choose == "1":
                print(tabulate(MentorModel.get_all_mentors(), headers= "", tablefmt='fancy_grid',stralign='center'))
            elif user_choose == "2":
                cls.add_new_mentor(cls)
            elif user_choose == "3":
                cls.remove_mentor(cls)
            elif user_choose == "4":
                print(Student.show_students_list())
            elif user_choose == "5":
                pass
            elif user_choose == "6":
                pass
            elif user_choose == "7":
                pass
            elif user_choose == "0":
                break
            else:
                print("Bad choice. Enter correct value.")

    def add_new_mentor(self):
        name = input("Type mentor name: ")
        while len(name) == 0:
            name = input("Name must not be empty: ")
        surname = input("Type surname")
        while len(surname) == 0:
            surname = input("Surname must not be empty: ")
        login = input("Type login")
        while len(login) == 0:
            name = input("Login must not be empty: ")
        MentorControl.add_mentor(name, surname, login)

    def remove_mentor(self):
        mentor_id = input("Type mentor id: ")
        while not mentor_id.isdigit():
            mentor_id = input("Student ID must be valid number: ")

        MentorControl.remove_mentor(mentor_id)
