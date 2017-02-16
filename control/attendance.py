# from attendance_model import AttendanceModel
import datetime


class AttendanceControl:

    @classmethod
    def add_attendance(cls, tuple_list, id_studenta, presence):
        attendance = (len(tuple_list)+1, str(datetime.date), presence, id_studenta)
        tuple_list.append(attendance)
        return tuple_list

    @classmethod
    def display_attendance(cls, tuple_list):
        tuple_list = [list(elem) for elem in tuple_list]
        return tuple_list

    def calculate_attendance(self):
        pass
