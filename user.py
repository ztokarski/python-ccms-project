from open_list import *


class User():
    '''
    Class for user.
    '''
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.login = name.lower()+surname.lower()
        self.password = name.lower()+"123"
        self.state = True

    def __str__(self):
        return "{} {} {} {}".format(self.name, self.surname, self.login, self.password)

    def change_state(self):
        '''
        change user's status (Activ/Disactiv)
        '''
        self.state = not self.state

    def display_state(self):
        if self.state == True:
            return("Activ")
        else:
            return("Disactiv")


class Student(User):
    '''
    Class for student.
    '''
    def __init__(self, name, surname):
        User.__init__(self, name, surname)

    def __str__(self):
        return "{} {} {} {} {}\n".format(self.name, self.surname, self.login, self.password, self.state)



class StudentList():
    '''
    Class for list of students.
    '''
    def __init__(self):
        self.students_list = []

    def __str__(self):
        all_students = ""
        for item in self.students_list:
            if item.state == True: # only Activ Students
                all_students += str(item)
        return all_students

    def display_sl(self, string):
        '''
        Making list of lists (lol) from string
        '''
        self.string = str(string)
        lol = [x.split(" ") for x in self.string.split("\n")]
        return lol[:-1]

    def display_ol(self, lol):
        '''
        Making list of objects (loo) from list of lists
        '''
        self.lol = lol
        self.loo = []
        for item in self.lol:
            obj = Student(item[0], item[1])
            obj.login = item[2]
            obj.password = item[3]
            obj.state = item[4]
            self.loo.append(obj)
        return self.loo


    def add_student(self, student):
        if isinstance (student, Student):
            self.students_list.append(student)

    def open_users(self, user_list):
        users_list = []
        read_file = open(user_list, "r")
        for user in read_file:
            users_list.append(user.strip().split(","))
        read_file.close()
        return list(users_list)

    def get_students_list(self):
        '''
        get students list from csv.file and return list of objects
        '''
        students_list = StudentList().open_users("CSV/students.csv")
        students_object_list = StudentList().display_ol(students_list)
        # for num, item in enumerate(students_object_list):
        #     print("{} {} {} {}".format(num+1, item.name, item.surname, item.state))
        return students_object_list
        # return students_list


class Employee(User):
    '''
    Class for Employee.
    '''
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return "{} {} {} {} {}\n".format(self.name, self.surname, self.login, self.password, self.state)


class Mentor(Employee):
    '''
    Class for Mentor.
    '''
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return "{} {} {} {} {}\n".format(self.name, self.surname, self.login, self.password, self.state)


class MentorList():
    '''
    Class for list of mentors.
    '''
    def __init__(self):
        self.mentors_list = []

    def __str__(self):
        all_mentors = ""
        for item in self.mentors_list:
            if item.state == True: # only Activ Mentors
                all_students += str(item)
        return all_students

    def display_sl(self, string):
        '''
        Making list of lists (lol) from string
        '''
        self.string = str(string)
        lol = [x.split(" ") for x in self.string.split("\n")]
        return lol[:-1]

    def display_ol(self, lol):
        '''
        Making list of objects (loo) from list of lists
        '''
        self.lol = lol
        self.loo = []
        for item in self.lol:
            obj = Mentor(item[0], item[1])
            obj.login = item[2]
            obj.password = item[3]
            obj.state = item[4]
            self.loo.append(obj)
        return self.loo


    def add_mentor(self, student):
        if isinstance (student, Student):
            self.students_list.append(student)

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
        # for num, item in enumerate(mentors_object_list):
        #     print("{} {} {} {}".format(num+1, item.name, item.surname, item.state))
        return mentors_object_list
        # return students_list


class Manager(Employee):
    '''
    Class for Manager.
    '''
    def __init__(self, name, surname):
        Employee.__init__(self, name, surname)

    def __str__(self):
        return "{} {} {} {} {}\n".format(self.name, self.surname, self.login, self.password)




'''TEST TEST TEST'''

# print(MentorList().get_mentors_list())
# StudentList().get_students_list()

# print(a)
#
# for item in a:
#     print (item)
# user1 = Student("Jan", "Kowalski")
# user2 = Student("Tomasz", "Nowak")
# user3 = Student("Adolf", "Dupa")
#
# students_list = StudentList()
#
# students_list.add_student(user1)
# students_list.add_student(user2)
# students_list.add_student(user3)
# print(students_list)
#
# lol = (students_list.display_sl(students_list))
# print(lol)
#
# loo = (students_list.display_ol(lol))
# print(loo)
# print(loo[0].name)
