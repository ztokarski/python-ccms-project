# from model.student_model import *
from flask import Flask, render_template, request
from configure import DATABASE as db

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

if __name__ == '__main__':
    app.run(debug=True)
