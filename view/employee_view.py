class EmployeeUI():
    def __init__(self, employee):
        self.employee = employee
    def show_employee_menu(self):
        while True:
            print(
                "\n/-----------------------"
                "\n| Mentor menu:"
                "\n| (1) Show students list.
                "\n| (2) Show Mentors list.
                "\n| (0) Exit"
                "\n\-----------------------"
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
            elif user_choose == "0":
                break
            else:
                print("Bad choice. Enter correct value.")