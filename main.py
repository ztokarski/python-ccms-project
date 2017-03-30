from flask import Flask, render_template, request, url_for, redirect, make_response, session
from model.assignments_model import *
from model.employee_model import *
from model.mentor_model import *
from model.student_model import *
from model.user_model import User_model
from model.user import *
import sqlite3

app = Flask(__name__)
app.secret_key = "npionWGOJPOJKWAFR1423508-';\/[;498yhdoiuajwfniol"


@app.route("/")
def index():
    session.clear()
    return render_template("index.html")

@app.route("/login", methods=["POST"])
@app.route("/invalid", methods=["GET"])
def login():
    if request.method == "POST":
        user_login = request.form["login"]
        user_id = User_model.get_id_from_login(user_login)
        print(user_id)
        if user_id == "There's no such user!":
            print("theres no such user!")
            return redirect("/login_error")
        else:
            user_object = User_model.get_object_by_id(user_id)
            cookies_dict = {"user_login": user_login, "user_name": user_object.name,
                            "user_surname": user_object.surname,
                            "user_id": user_object.id}
            if isinstance(user_object, Student):
                cookies_dict["user_role"] = "student"
            elif isinstance(user_object, Mentor):
                cookies_dict["user_role"] = "mentor"

            if isinstance(user_object, Employee):
                cookies_dict["user_role"] = "employee"
            if isinstance(user_object, Manager):
                cookies_dict["user_role"] = "manager"

            session.update(cookies_dict)
            print(session)

            return make_response(redirect("main"))

    else:
        return redirect(url_for("login_error"))


@app.route("/main")
def main():
    name = request.cookies.get("user_name")
    return render_template("main.html", name=name)



@app.route("/login_error")
def login_error():
    return render_template("login_error.html")


@app.route("/student_list", methods=["GET", "POST"])
def student_list():
    students = StudentModel.get_all_students()
    return render_template("student_list.html", students=students)


@app.route("/student_add")
def student_form():
    return render_template("student_add.html")


@app.route("/student_add", methods=["POST"])
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
        StudentModel.edit_student(student_with_new_data)

        return redirect(url_for("student_list"))


@app.route("/student_remove/<int:student_id>", methods=["GET", "POST"])
def remove_student(student_id):
    StudentModel.remove_student(student_id)
    return redirect(url_for("student_list"))


@app.route("/mentor_edit/<int:mentor_id>", methods=["POST", "GET"])
def mentor_edit(mentor_id):
    mentor_to_edit = User_model.get_object_by_id(mentor_id)
    if request.method == "GET":
        return render_template("mentor_edit.html", mentor=mentor_to_edit)
    elif request.method == "POST":
        mentor_with_new_data = Mentor(request.form["name"], request.form["surname"])
        mentor_with_new_data.login = request.form["login"]
        mentor_with_new_data.id = mentor_id
        MentorModel.edit_mentor(mentor_with_new_data)
        return redirect(url_for("mentor_list"))


@app.route("/mentor_list")
def mentor_list():
    mentors = MentorModel.get_all_mentors()
    return render_template("mentor_list.html", mentors=mentors)


@app.route("/mentor_add")
def mentor_form():
    return render_template("mentor_add.html")


@app.route("/mentor_remove/<int:mentor_id>", methods=["GET", "POST"])
def remove_mentor(mentor_id):
    MentorModel.remove_mentor(mentor_id)
    return redirect(url_for("mentor_list"))


@app.route("/mentor_add", methods=["POST"])
def submit_mentor():
    name = request.form["name"]
    surname = request.form["surname"]
    login = request.form["login"]
    my_mentor = Mentor(name, surname)
    my_mentor.login = login
    MentorModel.add_mentor(my_mentor)
    return redirect(url_for("mentor_list"))


@app.route("/assignment_list", methods=["GET", "POST"])
def assignment_list():
    assignments = AssignmentModel.get_assignments_list()
    return render_template("assignment_list.html", assignments=assignments)


@app.route("/assignment_add")
def assignment_form():
    return render_template("assignment_add.html")


@app.route("/assignment_add", methods=["POST"])
def submit_assignment():
    assignment_name = request.form["assignment_name"]
    due_date = request.form["due_date"]
    max_points = request.form["max_points"]
    my_assignment = Assignment(assignment_name, due_date, max_points)
    AssignmentModel.add_assignment(my_assignment)
    return redirect(url_for("assignment_list"))


@app.route("/assignment_edit/<int:ID_assignment>", methods=["POST", "GET"])
def assignment_edit(ID_assignment):
    assignment_to_edit = User_model.get_assignment_by_id(ID_assignment)
    if request.method == "GET":
        return render_template("assignment_edit.html", assignment=assignment_to_edit)
    elif request.method == "POST":
        assignment_with_new_data = Assignment(request.form["assignment_name"], request.form["due_date"],
                                              request.form["max_points"])
        # assignment_with_new_data.ID_assignment = request.form["ID_assignment"]
        AssignmentModel.edit_assignment(assignment_with_new_data)
        return redirect(url_for("assignment_list"))


@app.route("/assignment_remove/<int:ID_assignment>", methods=["GET", "POST"])
def remove_assignment(ID_assignment):
    AssignmentModel.remove_assignment(ID_assignment)
    return redirect(url_for("assignment_list"))


@app.route("/employee_list")
def employee_list():
    employees = EmployeeModel.get_all_employees()
    return render_template("employee_list.html", employees=employees)


@app.route("/employee_add")
def employee_form():
    return render_template("employee_add.html")


@app.route("/employee_add", methods=["POST"])
def submit_employee():
    name = request.form["name"]
    surname = request.form["surname"]
    login = request.form["login"]
    my_employee = Employee(name, surname)
    my_employee.login = login
    EmployeeModel.add_employee(my_employee)

    return redirect(url_for("employee_list"))


@app.route("/employee_edit/<int:employee_id>", methods=["POST", "GET"])
def employee_edit(employee_id):
    employee_to_edit = User_model.get_object_by_id(employee_id)
    if request.method == "GET":
        return render_template("employee_edit.html", employee=employee_to_edit)
    elif request.method == "POST":
        employee_with_new_data = Employee(request.form["name"], request.form["surname"])
        employee_with_new_data.login = request.form["login"]
        employee_with_new_data.id = employee_id
        print(employee_with_new_data)
        EmployeeModel.edit_employee(employee_with_new_data)
        return redirect(url_for("employee_list"))


@app.route("/employee_remove/<int:employee_id>", methods=["GET", "POST"])
def remove_employee(employee_id):
    EmployeeModel.remove_employee(employee_id)
    return redirect(url_for("employee_list"))


@app.route("/team_list.html")
def team_list():
    c = sqlite3.connect(app.database)
    conn = c.cursor()
    db_list = conn.execute("SELECT * FROM teams ")
    teams = []
    for row in db_list:
        teams.append(row)
    return render_template("team_list.html", teams=teams)


@app.route("/team_add")
def team_add():
    return render_template("team_add.html")


@app.route("/team_edit")
def team_edit():
    return render_template("team_edit.html")


if __name__ == '__main__':
    app.run(debug=True)

