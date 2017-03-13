
from view.login_view import *
from model.student_model import *
from flask import Flask, render_template, request

app = Flask(__name__)


# def main():
#     Login_view.login_password()

if __name__ == '__main__':
    app.run(debug=True)
