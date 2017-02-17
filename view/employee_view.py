from model.mentor_model import *
from model.student_model import *
from tabulate import tabulate

class EmployeeUI():
    def __init__(self, employee):
        self.employee = employee

    @classmethod
    def show_employee_menu(cls):
        while True:
            print(
                "\n/-----------------------"
                "\n| Mentor menu:"
                "\n| (1) Show students list."
                "\n| (2) Show Mentors list."
                "\n| (0) Exit"
                "\n\-----------------------"
            )
            user_choose = input('Your choose: ')
            if user_choose == "1":
                print(tabulate(StudentModel.get_all_students(), headers=['ID', "name", "surname"], tablefmt='fancy_grid',stralign='center'))
            elif user_choose == "2":
                print(tabulate(MentorModel.get_all_mentors(), headers="", tablefmt='fancy_grid', stralign='center'))
            elif user_choose == "0":
                break
            else:
                print("Bad choice. Enter correct value.")
