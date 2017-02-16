import sqlite3

class User_model:

    conn = sqlite3.connect('/home/lukasz/Pycharm/Projects/ccm/python-ccms-programadores/ccms.db')

    '''
    Class for user.
    '''

    def __init__(self, name, surname):
        self.id = 0
        self.name = name
        self.surname = surname
        self.login = None
        self.password = None
        self.status = 1
        self.id_role = 0
        self.id_team = 0

    def __repr__(self):
        return "ID: {} Name: {} Surname {} Status: {}".format(self.id, self.name, self.surname, self.status)


    @classmethod
    def get_all_users(cls):
        user_list = []

        for user in db_list:
            name = user[1]
            surname = user[2]
            user_object = User_model(name, surname)
            user_object.id = user[0]
            user_object.login = user[3]
            user_object.password = user[4]
            user_object.status = user[5]
            user_object.id_team = user[6]
            user_object.id_role = user[7]
            user_list.append(user_object)

        return user_list

    @classmethod
    def get_object_by_id(self, id):
        conn = sqlite3.connect('/home/lukasz/PycharmProjects/ccm/python-ccms-programadores/ccms.db')
        users = conn.execute("SELECT * FROM users WHERE ID_user == %i" % (int(id)))
        for user in users:
            name = user[1]
            surname = user[2]
            user_object = User_model(name, surname)
            user_object.id = user[0]
            user_object.login = user[3]
            user_object.password = user[4]
            user_object.status = user[5]
            user_object.id_team = user[6]
            user_object.id_role = user[7]

        return user_object

    def change_status(self):
        '''
        change user's status (Activ/Disactiv)
        '''
        self.status = not self.status

    def display_status(self):
        if self.status == True:
            return ("Activ")
        else:
            return ("Disactiv")


class Student(User):

    '''
    Class for student.
    '''
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.team = None
        self.grades_list = []

    def __str__(self):
        return "{} {} {} {} {}\n".format(self.name, self.surname, self.login, self.password, self.status)

    @classmethod
    def get_all_students(cls):
        list_of_students = []
        students = cls.conn.execute("SELECT * FROM users WHERE ID_role = `1`)
        for student in students:

            name = student[1]
            surname = student[2]
            student_object = Student(name, surname)
            student_object.id = student[0]
            student_object.login = student[3]
            student_object.password = student[4]
            student_object.status = student[5]
            student_object.id_team = student[6]
            student_object.id_role = student[7]
            list_of_students.append(student_object)

        return list_of_students



    def show_grades(self):
        '''
        Method which return student's grades.
        '''
        from_grades = Open().open_users("CSV/sub_assignments.csv")
        grades = {}
        for assigment in subs_assigment:
            if assigment.grade != None:
                grades[assigment.name] = assigment.grade

        return grades


    def submit_assignment(self, name):
        '''
        Method for submitting assignment
        '''
        assigment = Sub_assigment(name)
        assigment.date = "{}.{}.{}".format(time.localtime()[2], time.localtime()[1], time.localtime()[0])
        return assigment


    @staticmethod
    def add_student(*args):
        model = Student_model()
        model.add_student(args)

    @staticmethod
    def remove_student(student_id):
        model = Student_model()
        model.remove_student(student_id)

    @classmethod
    def show_students_list(cls):
        students = Student.get_students_list()
        return tabulate(students, headers=['ID', 'NAME', 'SURNAME', 'GROUP'], tablefmt='fancy_grid',
                   stralign='center')


class Mentor(User):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.list_of_mentors(self)

    @classmethod
    def get_all_mentors(cls):
        list_of_mentors = []
        mentors = cls.conn.execute("SELECT * FROM users WHERE ID_role = `2`)
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


from control.user import User

class Manager(User):
    '''
    Class for Manager.
    '''
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return "{}".format("BOSKI JUREK")


class Employee(User):
    def __init__(self, name, surname):
        super().__init__(name, surname)

        class Mentor_model:
            def __init__(self):
                self.conn = sqlite3.connect(os.path.realpath('../ccms.db'))
                self.db = self.conn.cursor()

            def get_mentors_list(self):
                mentors_list = self.db.execute("SELECT * FROM users where ID_role = 2")
                return mentors_list

            def add_mentor(self, *args):
                self.conn.execute(
                    "INSERT INTO `users`(`name`,`surname`,`login`, `ID_role`) VALUES ('{}','{}','{}', 2);".format(
                        *args))
                self.conn.commit()

            def remove_mentor(self, mentor_id):
                self.conn.execute("DELETE FROM users where ID_user = {}".format(mentor_id))
                # TODO trychatch if id not valid

        == == == =
        import control\students

        class Student_model:
            conn = sqlite3.connect('ccms.db')

            mentor_db = conn.execute("SELECT * FROM users WHERE id_role = 2")

            return mentor_db_db

        >> >> >> > submitted_assigments

        import sqlite3
        import os

        class Student_model:
            def __init__(self):
                self.conn = sqlite3.connect(os.path.realpath('../ccms.db'))
                self.db = self.conn.cursor()

            def get_students_list(self):
                students_list = self.db.execute("SELECT * FROM users where ID_role = 1")
                return students_list

            def add_student(self, *args):
                self.conn.execute(
                    "INSERT INTO `users`(`name`,`surname`,`login`) VALUES ('{}','{}','{}');".format(*args))
                self.conn.commit()

            def remove_student(self, student_id):
                self.conn.execute("DELETE FROM users where ID_user = {}".format(student_id))
                # TODO trychatch if id not valid


