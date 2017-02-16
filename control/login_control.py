from login_view import *


class Login_control:
    def __init__(self):
        self.login = ""
        self.password = ""


    @classmethod
    def get_login(self):
        return Login_view.login()

    @classmethod
    def get_password(cls):
        return Login_view.password()