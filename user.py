class User():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.login = name.lower()+surname.lower()
        self.password = name.lower()+"123"

    def __str__(self):
        return "{} {} {} {}".format(self.name, self.surname, self.login, self.password)


class Student(User):
    def __init__(self, name, surname):
        User.__init__(self, name, surname)
        # self.points = []

    def __str__(self):
        return "{} {} {} {}".format(self.name, self.surname, self.login, self.password)




    def add_points(self, points):
            self.points.append(points)

    def remove_points(self, points):
        try:
            self.points.remove(points)
        except ValueError as point_error:
            print(point_error)



class StudentList():
    def __init__(self):
        self.students_list = []

    def __str__(self):
        all_students = ""
        for item in self.students_list:
            all_students += str(item)
        return all_students

    def add_student(self, student):
        if isinstance (student, Student):
            self.students_list.append(student)




class Employee(User):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return "{} {} {} {}".format(self.name, self.surname, self.password)


            # def __str__(self):
            #     all_subject = " "
            #     for item in self.subject:
            #         all_subject += str(item)
            #     return Person.__str__(self) + " I teach {}.".format(all_subject)


def convert_str_to_list(string):
    return list(string.split(" "))

user1 = Student("Jan", "Kowalski")
user2 = Student("Tomasz", "Nowak" )

students_list = StudentList()
students_list.add_student(user1)
students_list.add_student(user2)
print(students_list)

# lista = convert_str_to_list(str(students_list))
# print(lista)
# a=["Adam","Kuś"]
#
# def Student_from_list(lista):
#     b=Student(lista[0], lista[1])
#     return b
#
# a=["Adam","Kuś"]
# print(Student_from_list(lista))


# user1.add_points(10); user1.add_points(20); user1.add_points(31)
# print(user1)
# print(user2)
#
# user2 = Student("Adam", "Nowak")
# user2.add_points(12); user2.add_points(24); user2.add_points(30)
# # print(user2)
#
# students_list = StudentList()
# students_list.add_student(user1)
# students_list.add_student(user2)
# students_list.add_student("koko")
#
# print(students_list)

