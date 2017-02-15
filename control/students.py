class Student(User):
    student_list = []
    '''
    Class for student.
    '''
    def __init__(self, name, surname):
        super().__init__(self, name, surname)
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