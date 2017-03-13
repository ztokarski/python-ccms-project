# from model.student_model import *
from flask import Flask, render_template, request
from configure import DATABASE as db
import sqlite3

app = Flask(__name__)
app.database = db

@app.route("/")
def index():
    return render_template("index.html")
# def main():
#     Login_view.login_password()

@app.route("/main.html")
def main():
    return render_template("main.html")

@app.route("/test")
def test():
    c = sqlite3.connect(app.database)
    conn = c.cursor()
    db_list = conn.execute("SELECT * FROM users;")
    my_list = []
    for row in db_list:

        my_list.append(row)

    return render_template("test_list.html", my_list=my_list)


if __name__ == '__main__':
    app.run(debug=True)
