from model.user_model import *
from db_connection import DB

class MentorModel(User_model):

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
    def add_mentor(self, mentor):
        data = DB.get_connection()
        cursor = data.cursor()
        cursor.execute("INSERT INTO 'users'('name','surname','login', 'ID_role') VALUES ('{}','{}','{}','{}');".format(mentor.name, mentor.surname, mentor.login, 2))
        data.commit()
        data.close()

    @classmethod
    def remove_mentor(self, mentor_id):
        data = DB.get_connection()
        cursor = data.cursor()
        cursor.execute("DELETE FROM users where ID_user = {} and ID_role = 2".format(mentor_id))
        data.commit()
        data.close()
        
    @classmethod
    def edit_mentor(cls, mentor):
        data = DB.get_connection()
        cursor = data.cursor()
        cursor.execute("UPDATE users SET name = ?, surname = ?, login = ? WHERE ID_user = ?", (mentor.name, mentor.surname, mentor.login, mentor.id))
        data.commit()
        data.close()