import os
from ui import *
from open_list import *
from login import *
from user import *
import sys
import csv


class Ui:
    """User interface - display all tables and menus"""

    START_MAIN = ("""
      ____          _                        _
     / ___|___   __| | ___    ___ ___   ___ | |
    | |   / _ \ / _` |/ _ \  / __/ _ \ / _ \| |
    | |__| (_) | (_| |  __/ | (_| (_) | (_) | |
     \____\___/ \__,_|\___|  \___\___/ \___/|_|
      __  __           _             __  __
     |  \/  |         (_)           |  \/  |
     | \  / |   __ _   _   _ __     | \  / |   ___   _ __    _   _
     | |\/| |  / _` | | | | '_ \    | |\/| |  / _ \ | '_ \  | | | |
     | |  | | | (_| | | | | | | |   | |  | | |  __/ | | | | | |_| |
     |_|  |_|  \__,_| |_| |_| |_|   |_|  |_|  \___| |_| |_|  \__,_|

    """)

    MANAGER_INTRO = ("""
    Logged as a Manager.
        Manager Menu.
            Witch option you want to select?
            #1. Show Mentors list.
            #2. Add new Mentor.
            #3. Remove Mentor.
            #4. Show students list.
            #5. Show Employees list.
            #0. Exit program
    """)

    MENTOR_INTRO = ("""
    Logged as a Mentor.
        Mentor Menu.
            Which option you want to select?
            #1. Check attendance.
            #2. Add student.
            #3. Remove student.
            #4. Show students list.
            #5. Add grade.
            #6. Update grade.
            #7. Show grades list.
            #0. Exit program
    """)

    STUDENT_INTRO = ("""
    Logged as a Student.
        Student Menu.
            Which option you want to select?
            #1. Show grades list.
            #2. Add assignment.
            #0. Exit program
    """)

    EMPLOYEE_INTRO = ("""
    Logged as a Employee.
        Employee Menu.
            Which option you want to select?
            #1. Show students list.
            #2. Show Mentors list.
            #3. Show grades list.
            #0. Exit program
    """)




class Menu:

    @classmethod
    def login_and_menu(self):
        user = Login.login_check()

        if isinstance(user, Student):
            print(user.name)
            print(user.surname)
            StudentMenu.student_menu(self, user.name, user.surname)
        else:
            raise ValueError("dupa")


class StudentMenu:
        def show_done(self, name, surname):
            undone = Open().open_users("CSV/assignments.csv")
            done = Open().open_users("CSV/sub_assignments.csv")
            user = User(name, surname)
            for submit in done:
                if submit[0] == user.name.lower() + user.surname.lower():
                    print("{} Grade: {} Date {}.".format(submit[1].title(), submit[2], submit[3]))

        def check_undone(self, name, surname):
            undone = Open().open_users("CSV/assignments.csv")
            done = Open().open_users("CSV/sub_assignments.csv")
            student_undone = undone
            user = User(name, surname)
            for submit in done:
                if submit[0] == user.name.lower() + user.surname.lower():
                    for x in student_undone:
                        if submit[1] == x[0]:
                            a = x
                            student_undone.remove(a)
            return student_undone


        def show_undone(self, undone):
            for num, dupa in enumerate(undone, 1):
                print("{}. {} - {}".format(num, dupa[0].title(), dupa[1]))

            arg = ""
            which_to_submit = input("Which position on the list would You like to submit?")

            for num, dupa in enumerate(undone, 1):
                if which_to_submit == str(num):
                    arg = str(dupa[0])

                    return arg
                else:
                    raise ValueError

        def student_menu(self, name, surname):
            print("dupa")
            user = User(name, surname)
            print(user)
            print("Hello, {}".format(name))
            print("")
            print(Ui.STUDENT_INTRO)
            option = input("Pick an option")
            # if option == "1":
            if option == "2":
                print("{} {}".format(user.name, user.surname))
                #StudentMenu.give_done(self, name, surname)
                StudentMenu.show_done(self, name, surname)
                check_undone = StudentMenu.check_undone(self, name, surname)
                assignment = StudentMenu.show_undone(self, check_undone)
                student = Student(name, surname)
                submitted_assigment = student.submit_assigment(assignment)
                done = Open().open_users("CSV/sub_assignments.csv")
                done.append(submitted_assigment)
                Open().save(done, "CSV/sub_assignments.csv")

#         submitted_assigment = student.submit_assigment(arg)


                # print("")
                # print("Done:")
                #     # print(num, assignment[0].title(), assignment[1].title())
                # # def show_done
                #
                # print("Undone:")
                #
                # student = Student(name, surname)
                # submitted_assigment = student.submit_assigment(arg)
                # done.append(submitted_assigment)
                # done = to co chce zapisać
                # drugi = gdzie to chce
                # with open("CSV/sub_assignments.csv", "w") as f:
                #     writer = csv.writer(f)
                #     writer.writerows(done)
