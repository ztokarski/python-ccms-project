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
            mentor_object = Mentor(mentor[1], mentor[2])
            mentor_object.id = mentor[0]
            mentor_object.login = mentor[3]
            mentor_object.password = mentor[4]
            mentor_object.status = mentor[5]
            mentor_object.id_team = mentor[6]
            mentor_object.id_role = mentor[7]
            list_of_mentors.append(mentor_object)
        data.close()
        return list_of_mentors


    @classmethod
    def show_mentors_list(cls):
        mentors = Mentor.get_mentors_list()
        return tabulate(mentors, headers=['ID', 'NAME', 'SURNAME'], tablefmt='fancy_grid',
                        stralign='center')

    @classmethod
    def add_mentor(self, mentor):
        data = DB.get_connection()
        cursor = data.cursor()
        cursor.execute("INSERT INTO `users`(`name`,`surname`,`login`) VALUES ('{}','{}','{}');".format(mentor.name, mentor.surname, mentor.login))
        data.commit()
        data.close()


    def remove_mentor(self, mentor_id):
        try:
            self.conn.execute("DELETE FROM users where ID_user = {} and ID_role = 2".format(mentor_id))
            self.conn.commit()
        except OperationalError:
            print("Cannot remove")

