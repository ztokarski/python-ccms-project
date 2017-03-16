from flask import Flask, render_template, request, url_for, redirect, make_response
from model.employee_model import *
from model.assignments_model import *
from model.student_model import *
from model.mentor_model import *
from model.user_model import User_model
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/set_cookie", methods=["POST", "GET"])
def set_cookie():
    if request.method == "POST":
        user_login = request.form["login"]
        user_id = User_model.get_id_from_login(user_login)
        if user_id == "There's no such user!":
            return redirect("set_cookie")
        else:
            user_object = User_model.get_object_by_id(user_id)

            response = make_response(redirect("main"))
            response.set_cookie("user_login", user_login)
            response.set_cookie("user_name", str(user_object.name))
            response.set_cookie("user_surname", str(user_object.surname))
            response.set_cookie("user_id", str(user_object.id))

            return response
    else:
        return render_template("index.html", message="Invalid login or password!")

@app.route("/main")
def main():
    name = request.cookies.get("user_name")
    return render_template("main.html", name=name)


@app.route("/student_list", methods=["GET", "POST"])
def student_list():
    students = StudentModel.get_all_students()
    return render_template("student_list.html", students=students)

@app.route("/add")
def student_form():
    return render_template("student_add.html")

@app.route("/add", methods=["POST"])
def submit_student():
    name = request.form["name"]
    surname = request.form["surname"]
    login = request.form["login"]
    my_student = Student(name, surname)
    my_student.login = login
    StudentModel.add_student(my_student)

    return redirect(url_for("student_list"))

@app.route("/student_edit/<int:student_id>", methods=["POST", "GET"])
def student_edit(student_id):
    student_to_edit = User_model.get_object_by_id(student_id)
    if request.method == "GET":
        return render_template("student_edit.html", student=student_to_edit)
    elif request.method == "POST":
        student_with_new_data = Student(request.form["name"], request.form["surname"])
        student_with_new_data.login = request.form["login"]
        student_with_new_data.id = student_id
        print(student_with_new_data)
        StudentModel.edit_student(student_with_new_data)

        return redirect(url_for("student_list"))




@app.route("/student_remove/<int:student_id>", methods=["GET", "POST"])
def remove_student(student_id):
    StudentModel.remove_student(student_id)
    return redirect(url_for("student_list"))


@app.route("/mentor_list.html")
def mentor_list():
    mentors = MentorModel.get_all_mentors()
    return render_template("mentor_list.html", mentors=mentors)

@app.route("/mentor_add.html")
def mentor_add():
    return render_template("mentor_add.html")

@app.route("/mentor_edit.html")
def mentor_edit():
    return render_template("mentor_edit.html")

@app.route("/assignment_list")
def assignment_list():
    assignments = AssignmentModel.get_assignments_list()
    return render_template("assignment_list.html", assignments=assignments)

@app.route("/assignment_add.html")
def assignment_add():
    return render_template("assignment_add.html")

@app.route("/assignment_edit.html")
def assignment_edit():
    return render_template("assignment_edit.html")



@app.route("/employee_list.html")
def employee_list():
    employees = EmployeeModel.get_all_employees()
    return render_template("employee_list.html", employees=employees)

@app.route("/employee_add.html")
def employee_add():
    return render_template("employee_add.html")

@app.route("/employee_edit.html")
def employee_edit():
    return render_template("employee_edit.html")



@app.route("/team_list.html")
def team_list():
    c = sqlite3.connect(app.database)
    conn = c.cursor()
    db_list = conn.execute("SELECT * FROM teams ")

    teams = []
    for row in db_list:
        teams.append(row)
    return render_template("team_list.html", teams=teams)

@app.route("/team_add.html")
def team_add():
    return render_template("team_add.html")

@app.route("/team_edit.html")
def team_edit():
    return render_template("team_edit.html")

if __name__ == '__main__':
    # database = db_connection.DB
    # database.execute("DROP TABLE IF EXISTS users;"
    #                  "CREATE TABLE users (ID_user PRIMARY KEY AUTOINCREMENT, name, surname, login, password, status, ID_role, status)
    # VALUES ())
    app.run(debug=True)

