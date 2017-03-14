import sqlite3
from configure import DATABASE as db
from flask import Flask , render_template , request

app = Flask(__name__)
app.database = db

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/main.html")
def main():
    return render_template("main.html")

@app.route("/student_list.html")
def student_list():
    c = sqlite3.connect(app.database)
    conn = c.cursor()
    db_list = conn.execute("SELECT * FROM users "
                            "WHERE ID_role = 1 ")
    students = []
    for row in db_list:
        students.append(row)
    return render_template("student_list.html" , students=students)

@app.route("/student_add.html")
def student_add():
    return render_template("student_add.html")

@app.route("/student_edit.html")
def student_edit():
    return render_template("student_edit.html")



@app.route("/mentor_list.html")
def mentor_list():
    c = sqlite3.connect(app.database)
    conn = c.cursor()
    db_list = conn.execute("SELECT * FROM users "
                            "WHERE ID_role = 2 ")
    mentors = []
    for row in db_list:
        mentors.append(row)
    return render_template("mentor_list.html", mentors=mentors)

@app.route("/mentor_add.html")
def mentor_add():
    return render_template("mentor_add.html")

@app.route("/mentor_edit.html")
def mentor_edit():
    return render_template("mentor_edit.html")



@app.route("/assignment_list.html")
def assignment_list():
    c = sqlite3.connect(app.database)
    conn = c.cursor()
    db_list = conn.execute("SELECT * FROM assignments ")

    assignments = []
    for row in db_list:
        assignments.append(row)
    return render_template("assignment_list.html", assignments=assignments)

@app.route("/assignment_add.html")
def assignment_add():
    return render_template("assignment_add.html")

@app.route("/assignment_edit.html")
def assignment_edit():
    return render_template("assignment_edit.html")



@app.route("/employee_list.html")
def employee_list():
    c = sqlite3.connect(app.database)
    conn = c.cursor()
    db_list = conn.execute("SELECT * FROM users "
                            "WHERE ID_role = 3 ")
    employees = []
    for row in db_list:
        employees.append(row)
    return render_template("employee_list.html", employees = employees)

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
    app.run(debug=True)

