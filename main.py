from ui import *
from open_list import *
from login import *
from user import *

object_list = StudentList().get_students_list()
object_list2 = MentorList().get_mentors_list()

def main():
    # while True:
        # print(Ui.START_MAIN)
        # Login().login_check()
    print(Open().print_table(object_list))
    print(Open().print_table(object_list2))
    # print(dir(object_list[0]))
if __name__ == '__main__':
    main()