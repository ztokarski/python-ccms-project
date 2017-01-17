class Open:
    @classmethod
    def open_students(self):
        students_list = []
        read_file = open("students.csv", "r")
        for student in read_file:
        students_list.append(student.strip().split("\t"))
        read_file.close()
        return students_list

    @classmethod
    def open_mentors(self):
        mentors_list = []
        read_file = open("Mentors.csv", "r")
        for mentor in read_file:
        mentors_list.append(mentor.strip().split("\t"))
        read_file.close()
        return mentors_list

    @classmethod
    def open_emplyees(self):
        employee_list = []
        read_file = open("employees.csv", "r")
        for employee in read_file:
        employee_list.append(employee.strip().split("\t"))
        read_file.close()
        return employee_list
