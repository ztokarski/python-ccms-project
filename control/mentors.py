from control.user import User

class Mentor(User):
    list_of_mentors = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.list_of_mentors(self)




    def add_mentor(self, student):
        '''
        Method for adding mentor to mentors_list
        '''
        if isinstance (mentor, Mentor):
            self.mentors_list.append(mentor)
        return mentors_list

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