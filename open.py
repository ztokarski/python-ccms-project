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
        read_file = open("mentors.csv", "r")
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

    def open_users(self, user_list):
        users_list = []
        read_file = open(user_list, "r")
        for user in read_file:
            users_list.append(user.strip().split(","))
        read_file.close()
        return list(users_list)
