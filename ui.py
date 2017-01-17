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
            Witch option you want to select?
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
            Witch option you want to select?
            #1. Show grades list.
            #2. Add assignment.
            #0. Exit program
    """)

    EMPLOYEE_INTRO = ("""
    Logged as a Employee.
        Employee Menu.
            Witch option you want to select?
            #1. Show students list.
            #2. Show Mentors list.
            #3. Show grades list.
            #0. Exit program
    """)
