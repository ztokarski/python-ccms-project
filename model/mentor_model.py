from model.user import *
import os
import sqlite3
from sqlite3 import OperationalError
from db_connection import DB


class MentorModel:
    @classmethod
    def get_all_mentors(cls):
        data = DB.get_connection()
        data.cursor()
        list_of_mentors = []
        mentors = data.execute("SELECT * FROM users WHERE ID_role = 2; ")

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
            list_of_mentors.append(mentor_object)

        return list_of_mentors


    @classmethod
    def show_mentors_list(cls):
        mentors = Mentor.get_mentors_list()
        return tabulate(mentors, headers=['ID', 'NAME', 'SURNAME'], tablefmt='fancy_grid',
                        stralign='center')

    def add_mentor(self, name, surname, login):
        self.conn.execute("INSERT INTO `users`(`name`,`surname`,`login`, `ID_role`) VALUES ('{}','{}','{}', 2);".format(name, surname, login))
        self.conn.commit()

    def remove_mentor(self, mentor_id):
        try:
            self.conn.execute("DELETE FROM users where ID_user = {} and ID_role = 2".format(mentor_id))
            self.conn.commit()
        except OperationalError:
            print("Cannot remove")

