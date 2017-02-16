from control.login_control import *
from view.mentor_view import *
from view.student_view import *

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
        login = input("Login: ")
        password = input("Password: ")

        user = Login_control.find_user(login, password)
        user_with_type = Login_control.identify_user(user)

        return user_with_type

    menu_type = login_password(cls)
    if isinstance(menu_type, Mentor):
        MentorUI.show_mentor_menu()
    elif isinstance(menu_type, Student_model):
        StudentUI.show_student_menu()



