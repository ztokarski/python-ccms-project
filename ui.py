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

    def student_menu(name, surname):
        print("Hello, {}".format(name))
        print("")
        print(Ui.STUDENT_INTRO)
        option = input("Pick an option")
        if option == "1":
        if option == "2":
            print("{} {}".format(user.name, user.surname))
            undone = Open().open_users("CSV/assignments.csv")
            done = Open().open_users("CSV/sub_assignments.csv")
            student_undone = undone
            print("")
            print("Done:")
                # print(num, assignment[0].title(), assignment[1].title())
            for submit in done:
                if submit[0] == user.name.lower() + user.surname.lower():
                    for x in student_undone:
                        if submit[1] == x[0]:
                            a = x
                            student_undone.remove(a)
                    print("{} Grade: {} Date {}.".format(submit[1].title(), submit[2], submit[3]))
                else:
                    continue
            print("Undone:")
            for num, dupa in enumerate(student_undone, 1):
                print("{}. {} - {}".format(num, dupa[0].title(), dupa[1]))

            arg = ""
            which_to_submit = input("Which position on the list would You like to submit?")

            for num, dupa in enumerate(student_undone, 1):
                if which_to_submit == str(num):
                    arg = str(dupa[0])
                else:
                    raise ValueError
            student = Student(name, surname)
            submitted_assigment = student.submit_assigment(arg)
            done.append(submitted_assigment)
            with open("CSV/sub_assignments.csv", "w") as f:
                writer = csv.writer(f)
                writer.writerows(done)
