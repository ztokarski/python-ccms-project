from view.employee_view import EmployeeUI
from control.students import Student

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
                "\n| (5) Show assignments list."
                "\n| (6) Add assignment to the list."
                "\n| (7) Update grade."
                "\n| (8) Show grades list."
                "\n| (9) Create student teams."
                "\n| (10) Add student to team."
                "\n| (11) List all students groups."
                "\n| (12) Add specific card for student."
                "\n| (13) See full report of students between dates."
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
                self.show_students_list()
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
        surname = input("Type surname")
        login = input("Type login")
        Student.add_student(name, surname, login)

    def remove_student(self):
        self.show_students_list()
        student_id = input("Type student ID")
        Student.remove_student(student_id)

    def add_assignment(self):
        '''do kontrolera'''
        pass
