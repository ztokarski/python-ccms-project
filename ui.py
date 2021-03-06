import os
from ui import *
from open_lists import *
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
                                    ____
      ,----..                    ,'  , `.  .--.--.
     /   /   \                ,-+-,.' _ | /  /    '.
    |   :     :            ,-+-. ;   , |||  :  /`. /
    .   |  ;. /           ,--.'|'   |  ;|;  |  |--`
    .   ; /--`    ,---.  |   |  ,', |  ':|  :  ;_
    ;   | ;      /     \ |   | /  | |  || \  \    `.
    |   : |     /    / ' '   | :  | :  |,  `----.   \\
    .   | '___ .    ' /  ;   . |  ; |--'   __ \  \  |
    '   ; : .'|'   ; :__ |   : |  | ,     /  /`--'  /
    '   | '/  :'   | '.'||   : '  |/     '--'.     /
    |   :    / |   :    :;   | |`-'        `--'---'
     \   \ .'   \   \  / |   ;/
      `---`      `----'  '---'

    """)

    MANAGER_INTRO = ("""
            < MANAGER MENU >

            #1. Show Mentors list.
            #2. Add new Mentor.
            #3. Remove Mentor.
            #4. Show students list.
            #5. Show Employees list.
            #0. Log out
            """)

    MENTOR_INTRO = ("""
            < MENTOR MENU >

            #1. Check attendance.
            #2. Add student.
            #3. Remove student.
            #4. Show students list.
            #5. Add grade.
            #6. Update grade.
            #7. Show grades list.
            #0. Log out
            """)

    STUDENT_INTRO = ("""
            < STUDENT MENU >

            #1. Show grades list.
            #2. Submit assignment.
            #0. Log out
            """)

    EMPLOYEE_INTRO = ("""
            < EMPLOYEE MENU >

            #1. Show students list.
            #2. Show Mentors list.
            #0. Log out
            """)




class Menu:

    @classmethod
    def login_and_menu(self):
        while True:
            os.system("printf '\033c'")
            print(Ui.START_MAIN)
            print("Sign in (or press Ctrl + C to exit from program.)")
            user = Login.login_check()

            if isinstance(user, Student):
                StudentMenu.student_menu(self, user.name, user.surname)

            elif isinstance(user, Mentor):
                MentorMenu.mentor_menu(self, user.name, user.surname)

            elif isinstance(user, Employee):
                EmployeeMenu.employee_menu(self, user.name, user.surname)

            elif isinstance(user, Manager):
                ManagerMenu.manager_menu(self, user.name, user.surname)


class EmployeeMenu:
    def employee_menu(self, name, surname):

        not_exit = True
        while not_exit == True:
            object_table = StudentList.get_students_list(self)
            mentor_table = MentorList.get_mentors_list(self)
            user = User(name, surname)
            print(user)
            print("Hello, {}".format(name))
            print("")
            os.system("printf '\033c'")
            print(Ui.EMPLOYEE_INTRO)
            option = input("Pick an option")
            if option == "1":
                os.system("printf '\033c'")
                print(Display().print_table(object_table))
                print("")
                exit = input("Press ENTER to exit")
                # list_of_student = StudentList.print_students_list(self)
            if option == "2":
                os.system("printf '\033c'")
                # list_of_mentors = MentorList.print_mentors_list(self)
                print(Display().print_table(mentor_table))
                print("")
                exit = input("Press ENTER to continue")
                print("")

            elif option == "0":
                not_exit = False
            else:
                print("It's not a valid option!")

        Menu.login_and_menu()
                # object_students = StudentList.display_ol(self, list_of_student)
                # tabble_students = Display.print_table(self, object_students)



class MentorMenu:

    def mentor_menu(self, name, surname):
        """Option menu for mentor"""
        object_attendance = StudentList().get_students_list()
        user = User(name, surname)
        print("Hello, {} \n".format(name))
        print(Ui.MENTOR_INTRO)
        option = input("Pick an option")

        if option == "1":
            # Show attendance list
            print(Display().print_table(object_attendance))
            exit = input("Press ENTER to exit")
        elif option == "2":
            pass
        elif option == "3":
            pass
        elif option == "4":
            # Show students list
            print(Display().print_table(object_students))
        elif option == "5":
            pass
        elif option == "6":
            pass
        elif option == "7":
            pass
        elif option == "0":
            # Exit to main manu
            Menu().login_and_menu()
class ManagerMenu:
    def manager_menu(self, name, surname):
        print("\nWELCOME TO MANAGER MENU")
        user = User(name, surname)
        print(user)
        print("Hello, {}".forma(name))
        print("")
        print(Ui.MANAGER_INTRO)
        option = input("Your choose: ")

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
                if dupa[0] == "Name":
                    continue
                else:
                    print("{}. {} - {}".format(num, dupa[0].title(), dupa[1]))

            arg = ""
            which_to_submit = input("Which position on the list would You like to submit? (or type 0 to go back) ")
            if which_to_submit == "0":
                StudentMenu.student_menu(name, surname)
            else:
                for num, a in enumerate(undone, 1):
                    if which_to_submit == str(num):
                        arg = str(a[0])

                        return arg
                    else:

                        raise ValueError

        def student_menu(self, name, surname):
            os.system("printf '\033c'")
            not_exit = True
            while not_exit == True:
                user = User(name, surname)
                print("Hello, {}".format(name))
                print(Ui.STUDENT_INTRO)
                option = input("Pick an option")
                if option == "1":
                    os.system("printf '\033c'")
                    print("")
                    user = Student(name, surname).show_grades_list()
                    for subject in user:
                            print("{} Points: {} Date: {}".format(subject[1].title(), subject[2], subject[3]))
                    print("")
                    back = input("Press ENTER to go back")
                    os.system("printf '\033c'")

                elif option == "2":
                    os.system("printf '\033c'")
                    print("")
                    print("{} {}".format(user.name, user.surname))
                    print("")
                    print("Submitted assigments:")
                    print("")
                    StudentMenu.show_done(self, name, surname)
                    check_undone = StudentMenu.check_undone(self, name, surname)
                    print("")
                    print("Assigments yet to submit:")
                    print("")
                    assignment = StudentMenu.show_undone(self, check_undone)
                    student = Student(name, surname)
                    submitted_assigment = student.submit_assigment(assignment)
                    done = Open().open_users("CSV/sub_assignments.csv")
                    done.append(submitted_assigment)
                    Open().save(done, "CSV/sub_assignments.csv")
                    print("")
                    back = input("Press ENTER to go back")
                elif option == "0":
                    not_exit = False
                else:
                    print("Invalid option!")