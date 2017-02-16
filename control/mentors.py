from control.user import User
from model.mentor_model import Mentor_model
from tabulate import tabulate

class Mentor(User):
    list_of_mentors = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.list_of_mentors(self)

    @staticmethod
    def add_mentor(cls, *args):
        model = Mentor_model()
        model.add_mentor(args)

    def open_users(self, user_list):
        users_list = []
        read_file = open(user_list, "r")
        for user in read_file:
            users_list.append(user.strip().split(","))
        read_file.close()
        return list(users_list)

    @staticmethod
    def get_mentors_list():
        mentors = []
        model = Mentor_model()

        for mentor in model.get_mentors_list():
            mentors.append([mentor[0], mentor[1], mentor[2]])
        return mentors

    @staticmethod
    def remove_mentor(mentor_id):
        model = Mentor_model()
        model.remove_mentor(mentor_id)

    @classmethod
    def show_mentors_list(cls):
        mentors = Mentor.get_mentors_list()
        return tabulate(mentors, headers=['ID', 'NAME', 'SURNAME'], tablefmt='fancy_grid',
                        stralign='center')

