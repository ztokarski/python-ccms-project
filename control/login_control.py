from view.login_view import *
from model.user_model import *
from model.mentor_model import *
from control.mentors import *
from employee import *

class Login_control:

    @classmethod
    def find_user(self, login, password):
        user_list = User_model.get_all_objects()
        login_input = Login_view.login()
        for object in user_list:
            if object.login == login and object.password == password:
                return object

        return "There's no such login!"

    @classmethod
    def identifie_object(cls, object):
        if object.id_role == 1:
            student = Student_model(object.name, object.surname)

            return student
        elif object.id_role == 2:
            mentor = Mentor(object.name, object.surname)

            return mentor

        elif object.id_role == 3:
            employee = Employee(object.name, object.surname)

            return employee

