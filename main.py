from model.student_model import *
from flask import Flask, render_template, request
# from configure import DATABASE as db
import sqlite3
import db_connection

app = Flask(__name__)
# app.database = db

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/test")
def test():
    c = sqlite3.connect(app.database)
    conn = c.cursor()
    db_list = conn.execute("SELECT * FROM users WHERE ID_role = 1 ")
    my_list = []
    for row in db_list:
        my_list.append(row)
    return render_template("test_list.html", my_list=my_list)



@app.route("/student_list")
def student_list():
    list_of_students = StudentModel.get_all_students()
    return render_template("student_list.html", lista=list_of_students)

@app.route("/student_add")
def student_form():
    return render_template("student_add.html")

@app.route("/student_add", methods=["POST"])
def submit_student():

    name = request.form["name"]
    surname = request.form["surname"]
    login = request.form["login"]
    test_list = []
    test_list.append(name)
    test_list.append(surname)
    test_list.append(login)
    return render_template("/test_from.html", lista=test_list)

@app.route("/student_edit")
def student_edit():
    return render_template("test.html")



@app.route("/mentor_list")
def mentor_list():
    return render_template("mentor_list.html")

@app.route("/mentor_add")
def mentor_add():
    return render_template("mentor_add.html")

@app.route("/mentor_edit")
def mentor_edit():
    return render_template("mentor_edit.html")



@app.route("/assignment_list")
def assignment_list():
    return render_template("assignment_list.html")

@app.route("/assignment_add")
def assignment_add():
    return render_template("assignment_add.html")

@app.route("/assignment_edit")
def assignment_edit():
    return render_template("assignment_edit.html")



@app.route("/employee_list")
def employee_list():
    c = sqlite3.connect(app.database)
    conn = c.cursor()
    db_list = conn.execute("SELECT * FROM users WHERE ID_role = 3 ")
    employees = []
    for row in db_list:
        employees.append(row)
    return render_template("employee_list.html", employees = employees)

@app.route("/aemployee_add")
def employee_add():
    return render_template("employee_add.html")

@app.route("/employee_edit")
def employee_edit():
    return render_template("employee_edit.html")




if __name__ == '__main__':
    database = db_connection.DB
    database.execute("DROP TABLE IF EXISTS users")
    app.run(debug=True)
