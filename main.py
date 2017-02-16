# import os
# from login import *
# from user import *
import sys
import csv
from model.attendance_model import AttendanceModel
from control.attendance import AttendanceControl
from tabulate import tabulate
from db_dump import clear_and_insert_db

def main():
    clear_and_insert_db()

if __name__ == '__main__':
    main()
