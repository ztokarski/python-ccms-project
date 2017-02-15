from control.user import User
from model.mentor_model import Mentor_model

class Mentor(User):
    list_of_mentors = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.list_of_mentors(self)



    @staticmethod
    def add_mentor(cls, *args):
        model =  Mentor_model()
        model.add_mentor(args)

    def open_users(self, user_list):
        users_list = []
        read_file = open(user_list, "r")
        for user in read_file:
            users_list.append(user.strip().split(","))
        read_file.close()
        return list(users_list)


    def get_mentors_list(self):
            '''
            get mentors list from csv.file and return list of objects
            '''
            mentors_list = MentorList().open_users("CSV/mentors.csv")
            mentors_object_list = MentorList().display_ol(mentors_list)
            return mentors_object_list

    def print_mentors_list(self):
        '''
        print mentors list
        '''
        print("< MENTORS LIST >\n")
        print_mentors_list = MentorList().get_mentors_list()
        for num, item in enumerate(print_mentors_list):
            print("{} {} {}".format(num+1, item.name, item.surname))

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