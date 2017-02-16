from model.user import *

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
                print(Student.show_students_list())
            elif user_choose == "2":
                print(Mentor.show_mentors_list())
            elif user_choose == "3":
                pass
            elif user_choose == "4":
                pass
            elif user_choose == "5":
                pass
            elif user_choose == "0":
                break
            else:
                print("Bad choice. Enter correct value.")
