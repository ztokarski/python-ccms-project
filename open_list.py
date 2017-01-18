class Open:
<<<<<<< HEAD
=======

>>>>>>> d78ea0c1545a86aa470446fbaeb4665fb4ac6131
    def open_users(self, user_list):
        users_list = []
        read_file = open(user_list, "r")
        for user in read_file:
            users_list.append(user.strip().split(","))
<<<<<<< HEAD
            read_file.close()
            return list(users_list)
=======
        read_file.close()
        return list(users_list)
>>>>>>> d78ea0c1545a86aa470446fbaeb4665fb4ac6131
