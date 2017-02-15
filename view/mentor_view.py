from view.employee_view import EmployeeUI

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
                pass
            elif user_choose == "3":
                pass
            elif user_choose == "4":
                pass
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