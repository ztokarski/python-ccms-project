from control.login_control import *
from view.mentor_view import *
from view.student_view import *
from view.employee_view import *
from view.manager_view import *

class Login_view:

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

    @classmethod
    def login_password(cls):
        print(cls.START_MAIN)
        login = input("Login: ")
        password = input("Password: ")

        user = Login_control.find_user(login, password)
        user_with_type = Login_control.identify_user(user)
        print(user_with_type)
        cls.menu_check(user_with_type)
        return user_with_type

    @classmethod
    def menu_check(cls, user_with_type):
        if isinstance(user_with_type, Mentor):
            MentorUI.show_mentor_menu()
        elif isinstance(user_with_type, Student):
            StudentUI.show_student_menu()
        elif isinstance(user_with_type, Employee):
            EmployeeUI.show_employee_menu()
        elif isinstance(user_with_type, Manager):
            ManagerUI.show_manager_menu()



