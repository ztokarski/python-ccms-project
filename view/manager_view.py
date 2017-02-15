from view.employee_view import EmployeeUI

class ManagerUI(EmployeeUI):
    def __init__(self, manager):
        super().__init__(manager)

    def show_manager_menu(self):
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
                self.show_mentors_list()
            elif user_choose == "2":
                pass
            elif user_choose == "3":
                pass
            elif user_choose == "4":
                self.show_students_list()
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
