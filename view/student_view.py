class StudentUI():
    def __init__(self, student):
        self.student = student
    def show_student_menu(self):
        while True:
            print(
                "\n/--------------------------------"
                "\n| Student menu:"
                "\n| (1) Show my grades."
                "\n| (2) See my overall attendance."
                "\n| (3) Submit assignment."
                "\n| (4) Submit team assignment."
                "\n| (0) Exit"
                "\n\--------------------------------"
            )
            user_choose = input('Your choose: ')
            if user_choose == "1":
                pass
            elif user_choose == "2":
                pass
            elif user_choose == "3":
                pass
            elif user_choose == "4":
                pass
            elif user_choose == "5":
                pass
            elif user_choose == "0":
                break
            else:
                print("Bad choice. Enter correct value.")



