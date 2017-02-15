
import os
from ui import *
from open_lists import *
from login import *
import sys
import time

class User:
    list_of_users = []
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
        self.list_of_users.append(self)

    def __str__(self):
        return "{} {} {} {}".format(self.name, self.surname)

    def change_status(self):
        '''
        change user's status (Activ/Disactiv)
        '''
        self.status = not self.status

    def display_status(self):
        if self.status == True:
            return("Activ")
        else:
            return("Disactiv")


class Student(User):
    student_list = []
    '''
    Class for student.
    '''
    def __init__(self, name, surname):
        super().__init__(self, name, surname)
        self.team = None
        self.grades_list = []
        self.student_list.append(self)


    def __str__(self):
        return "{} {} {} {} {}\n".format(self.name, self.surname, self.login, self.password, self.status)


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
        # assigment.student = student
        assigment.date = "{}.{}.{}".format(time.localtime()[2], time.localtime()[1], time.localtime()[0])
        return assigment

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

