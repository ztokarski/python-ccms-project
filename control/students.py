from control.user import User
from model.student_model import Student_model

class Student(User):
    student_list = []
    '''
    Class for student.
    '''
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.team = None
        self.grades_list = []
        self.student_list.append(self)


    def __str__(self):
        return "{} {} {} {} {}\n".format(self.name, self.surname, self.login, self.password, self.status)


    def show_grades(self):
        '''
        Method which return student's grades.
        '''
        from_grades = Open().open_users("CSV/sub_assignments.csv")
        grades = {}
        for assigment in subs_assigment:
            if assigment.grade != None:
                grades[assigment.name] = assigment.grade

        return grades


    def submit_assignment(self, name):
        '''
        Method for submitting assignment
        '''
        assigment = Sub_assigment(name)
        # assigment.student = student
        assigment.date = "{}.{}.{}".format(time.localtime()[2], time.localtime()[1], time.localtime()[0])
        return assigment

    @staticmethod
    def get_students_list():
        student_list = []
        model = Student_model()

        for student in model.get_students_list():
            student_list.append([student[0], student[1], student[2], student[7]])

        return student_list

    @staticmethod
    def add_student(*args):
        model =  Student_model()
        model.add_student(args)

    @staticmethod
    def remove_student(student_id):
        model = Student_model()
        model.remove_student(student_id)