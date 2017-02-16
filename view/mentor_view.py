from view.employee_view import EmployeeUI
from control.students import Student
from control.mentors import Mentor

class MentorUI(EmployeeUI):
    def __init__(self, mentor):
        super().__init__(mentor)
    def show_mentor_menu(self):
        while True:
            print(
                "\n/----------------------------------------------------"
                "\n| Mentor menu:"
                "\n| (1) Check attendance."
                "\n| (2) Add student."
                "\n| (3) Remove student."
                "\n| (4) Show students list."
                "\n| (5) Add grade."
                "\n| (6) Update grade."
                "\n| (7) Show grades list."
                "\n| (8) Create student teams."
                "\n| (9) Add student to team."
                "\n| (10) List all students groups."
                "\n| (11) Add specific card for student."
                "\n| (12) See full report of students between dates."
                "\n| (0) Exit"
                "\n\----------------------------------------------------"
            )
            user_choose = input('Your choose: ')

            if user_choose == "1":
                pass
            elif user_choose == "2":
                self.add_new_student()
            elif user_choose == "3":
                self.remove_student()
            elif user_choose == "4":
                print(Student.show_students_list())
            elif user_choose == "5":
                pass
            elif user_choose == "6":
                pass
            elif user_choose == "7":
                pass
            elif user_choose == "8":
                pass
            elif user_choose == "9":
                pass
            elif user_choose == "10":
                pass
            elif user_choose == "11":
                pass
            elif user_choose == "12":
                pass
            elif user_choose == "0":
                break
            else:
                print("Bad choice. Enter correct value.")

    def add_new_student(self):
        name = input("Type student name: ")
        while len(name) == 0:
            name = input("Name must not be empty: ")
        surname = input("Type surname: ")
        while len(surname) == 0:
            surname = input("Surname must not be empty: ")
        login = input("Type login: ")
        while len(login) == 0:
            name = input("Login must not be empty: ")
        Student.add_student(name, surname, login)

    def remove_student(self):
        self.show_students_list()
        student_id = input("Type student ID: ")
        while not student_id.isdigit():
            student_id = input("Student ID mus: ")
        Student.remove_student(student_id)

