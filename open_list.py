import csv

class Open:

    def open_users(self, user_list):
        users_list = []
        read_file = open(user_list, "r")
        for user in read_file:
            users_list.append(user.strip().split(","))
        read_file.close()
        return list(users_list)

    def save(self, updated_list, user_list):
        with open(user_list, "w") as f:
            writer = csv.writer(f)
            writer.writerows(updated_list)
