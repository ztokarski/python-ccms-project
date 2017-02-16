import sqlite3

class Login:
    @classmethod
    def login_check(self):
        login1 = input("Login: ")
        password1 = input("Password: ")

        conn = sqlite3.connect('/home/lukasz/PycharmProjects/ccm/python-ccms-programadores/ccms.db')
        login_password = conn.execute("SELECT * FROM users WHERE login = '{}' AND password = '{}'".format(login1, password1))
        user = None
        for i in login_password:
            user = i


Login.login_check()

