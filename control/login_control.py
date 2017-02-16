from model.user_model import *
from model.user import *
from view.login_view import *

class Login_control:

    @classmethod
    def find_user(self, login, password):
        user_list = User_model.get_all_users()
        for object in user_list:
            if object.login == login and object.password == password:
                return object

        return "There's no such login!"

    @classmethod
    def identify_user(cls, object):
        try:
            if object.id_role == 1:
                student = Student(object.name, object.surname)

                return student
            elif object.id_role == 2:
                mentor = Mentor(object.name, object.surname)

                return mentor

            elif object.id_role == 3:
                employee = Employee(object.name, object.surname)

                return employee

            elif object.id_role == 4:
                manager = Manager(object.name, object.surname)

                return manager
        except AttributeError:
            print("There's no such login!")



