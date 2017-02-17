from control.user import User
from model.mentor_model import MentorModel

class MentorControl(User):
    @classmethod
    def add_mentor(cls, name, surname, login):
        model = MentorModel()
        model.add_mentor(name, surname, login)

    @staticmethod
    def remove_mentor(mentor_id):
        model = MentorModel()
        model.remove_mentor(mentor_id)

