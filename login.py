from open import *


from open import *


class Login:


    def login_check(self):

        valid = ""
        valid_pass = ""

        while valid == "":
            login = input("Login: ")
            password = input("Password: ")

            for student in Open().open_users("students.csv"):
                if student[2] == login:
                    valid = student[2]
                    valid_pass = student[3]
                    if password == valid_pass:
                        print("student")
            for mentor in Open().open_users("mentors.csv"):
                if mentor[2] == login:
                    valid = mentor[2]
                    valid_pass = mentor[3]
                    if password == valid_pass:
                        print("mentor")
            for employee in Open().open_users("employees.csv"):
                if employee[2] == login:
                    valid = employee[2]
                    valid_pass = employee[3]
                    if password == valid_pass:
                        print("employee")
            print("Your login or password is incorrect.")
