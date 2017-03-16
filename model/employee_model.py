from model.user import Employee
from db_connection import DB


class EmployeeModel():
    @classmethod
    def get_all_employees(cls):
        data = DB.get_connection()
        data.cursor()
        list_of_employees = []
        employees = data.execute("SELECT * FROM users WHERE ID_role = 3; ")

        for employee in employees:
            name = employee[1]
            surname = employee[2]
            employee_object = Employee(name, surname)
            employee_object.id = employee[0]
            employee_object.login = employee[3]
            employee_object.password = employee[4]
            employee_object.status = employee[5]
            employee_object.id_team = employee[6]
            employee_object.id_role = employee[7]
            list_of_employees.append(employee_object)

        return list_of_employees

    @classmethod
    def add_employee(self, employee):
        data = DB.get_connection()
        cursor = data.cursor()
        cursor.execute("INSERT INTO `users`(`name`,`surname`,`login`,'ID_role') VALUES ('{}','{}','{}','{}');".format(employee.name, employee.surname, employee.login,3))
        data.commit()
        data.close()
