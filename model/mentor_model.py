from model.user import *
import os
import sqlite3
from sqlite3 import OperationalError


class MentorModel:

    conn = sqlite3.connect(os.path.realpath('ccms.db'))
    cursor = conn.cursor()

    @classmethod
    def get_all_mentors(cls):
        list_of_mentors = []
        mentors = cls.conn.execute("SELECT * FROM users "
                                   "WHERE ID_role = 2 ")

        for mentor in mentors:
            name = mentor[1]
            surname = mentor[2]
            mentor_object = Mentor(name, surname)
            mentor_object.id = mentor[0]
            mentor_object.login = mentor[3]
            mentor_object.password = mentor[4]
            mentor_object.status = mentor[5]
            mentor_object.id_team = mentor[6]
            mentor_object.id_role = mentor[7]
            list_object= []
            list_object.append(mentor_object)
            list_of_mentors.append(list_object)

        return list_of_mentors



    @classmethod
    def show_mentors_list(cls):
        mentors = Mentor.get_mentors_list()
        return tabulate(mentors, headers=['ID', 'NAME', 'SURNAME'], tablefmt='fancy_grid',
                        stralign='center')
    @classmethod
    def create_team(self, team_name):
        value = {'name':team_name}
        persistance.insert_data('Teams', value)


    def add_mentor(self, name, surname, login):
        self.conn.execute("INSERT INTO `users`(`name`,`surname`,`login`, `ID_role`) VALUES ('{}','{}','{}', 2);".format(name, surname, login))
        self.conn.commit()


    def remove_mentor(self, mentor_id):
        try:
            self.conn.execute("DELETE FROM users where ID_user = {} and ID_role = 2".format(mentor_id))
        except OperationalError:
            print("Cannot remove")
