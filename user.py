
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
        self.name = name
        self.surname = surname
        self.login = None
        self.password = None
        self.state = True
        self.list_of_users.append(self)


    def __str__(self):
        return "{} {} {} {}".format(self.name, self.surname)

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
    student_list = []
    '''
    Class for student.
    '''
    def __init__(self, name, surname):
        super().__init__(self, name, surname)
        self.student_list.append(self)
        self.grades_list = []

    def __str__(self):
        return "{} {} {} {} {}\n".format(self.name, self.surname, self.login, self.password, self.state)


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


class Manager(Employee):
    '''
    Class for Manager.
    '''
    def __init__(self, name, surname):
        Employee.__init__(self, name, surname)

    def __str__(self):
        return "{} {} {} {} {}\n".format(self.name, self.surname, self.login, self.password)


class Display:

    def fill_with_spaces(self, element, lenght):
        """ Fills table cell with space to desired length"""
        element = "|   " + element
        while len(element) < lenght:
            element += " "
        return element


    def print_table(self, object_list):
        """
        This method returns shapes list as string formatted into table. This is sample output:
         #---------------------------------------------------------------------------------#
         |  Name   |       Surname  |       Login          |   Password   |   Attendance   |
         |---------|----------------|----------------------|--------------|----------------|
         |  Jakub  |     Krzciuk    |    jakubkrzciuk      |  jakub123    |     True       |
         |---------|----------------|----------------------|--------------|----------------|
         |Sebastian|     Znaj       |    sebastianznaj     | sebastian123 |     True       |
         #---------------------------------------------------------------------------------#
        """

        # Body
        table_element = ""
        middle_rib = ("|" + "-" * 4) + ("|" + "-" * 19) * 2  + "|"
        for i, object in enumerate(object_list):
            if i == 0:
                Lp = "| Lp."
            else:
                Lp = "| " + str(i) + "."
                while len(Lp) < 5:
                    Lp += " "
            element = self.fill_with_spaces(object.name, 20)
            element1 = self.fill_with_spaces(object.surname, 20)
            # element2 = self.fill_with_spaces(object.state, 10)
            table_element += Lp + element + element1 + "|" + "\n" + middle_rib + "\n"

        # Frames
        table_lenght = "-" * (len(middle_rib) - 2)
        table_bottom = "#" + table_lenght + "#"
        table_top = "#" + table_lenght + "#"

        resoult = table_top + "\n" + table_element[:-(len(middle_rib)+2)] + "\n" + table_bottom + "\n"
        return resoult


