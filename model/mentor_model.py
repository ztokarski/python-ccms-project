from model.user import *

class Mentor_model:
    @classmethod
    def get_all_mentors(cls):
        list_of_mentors = []
        mentors = cls.conn.execute("SELECT * FROM users WHERE ID_role = `2`")

        for mentor in mentors:
            name = mentor[1]
            surname = mentor[2]
            student_object = Mentor(name, surname)
            mentor_object.id = mentor[0]
            mentor_object.login = mentor[3]
            mentor_object.password = mentor[4]
            mentor_object.status = mentor[5]
            mentor_object.id_team = mentor[6]
            mentor_object.id_role = mentor[7]
            list_of_mentors.append(mentor_object)

        return list_of_mentors

    @staticmethod
    def add_mentor(cls, *args):
        model = Mentor_model()
        model.add_mentor(args)

        @staticmethod
        def remove_mentor(mentor_id):
            model = Mentor_model()
            model.remove_mentor(mentor_id)

        @classmethod
        def show_mentors_list(cls):
            mentors = Mentor.get_mentors_list()
            return tabulate(mentors, headers=['ID', 'NAME', 'SURNAME'], tablefmt='fancy_grid',
                            stralign='center')