from open_lists import *
from user import *

class Login:
    @classmethod
    def login_check(self):

        valid = ""
        valid_pass = ""

        while valid == "":
            login = input("Login: ")
            password = input("Password: ")
            students = Open.open_users("CSV/students.csv")
            for student in students:
                if student[2] == login:
                    valid = student[2]
                    valid_pass = student[3]
                    if password == valid_pass:
                        login_student = Student(student[0], student[1])
                        return login_student

            for mentor in Open().open_users("CSV/mentors.csv"):
                if mentor[2] == login:
                    valid = mentor[2]
                    valid_pass = mentor[3]
                    if password == valid_pass:
                        login_mentor = Mentor(mentor[0], mentor[1])
                        return login_mentor

            for employee in Open().open_users("CSV/employees.csv"):
                if employee[2] == login:
                    valid = employee[2]
                    valid_pass = employee[3]
                    if password == valid_pass:
                        login_employee = Employee(employee[0], employee[1])
                        return login_employee
            print("Your login or password is incorrect.")
