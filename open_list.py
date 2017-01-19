import csv
from user import *

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




    def print_table(self, object_list):
        """
        This method returns shapes list as string formatted into table. This is sample output:
        ~~~
         /--------------------------------------------------------------------------------\
         |  Name   |       Surname  |       Login          |   Password   |   Attendence   |
         |---------|----------------|----------------------|--------------|----------------|
         |  Jakub  |     Krzciuk    |    jakubkrzciuk      |  jakub123    |     True       |
         |---------|----------------|----------------------|--------------|----------------|
         |Sebastian|     Znaj       |    sebastianznaj     | sebastian123 |     True       |
         \--------------------------------------------------------------------------------/
        ~~~
        """

        # Body
        table_element = ""
        middle_rib = ("|" + "-" * 4) + ("|" + "-" * 19) * 2 + ("|" + "-" * 9) + "|"
        for i, object in enumerate(object_list):
            if i == 0:
                Lp = "| Lp."
            else:
                Lp = "| " + str(i) + "."
                while len(Lp) < 5:
                    Lp += " "
            element = "|   " + object.name
            while len(element) < 20:
                element += " "
            element1 = "|   " + object.surname
            while len(element1) < 20:
                element1 += " "
            element2 = "|   " + object.state
            while len(element2) < 10:
                element2 += " "
            table_element += Lp + element + element1 + element2 + "|" + "\n" + middle_rib + "\n"

        # Frames
        table_lenght = "-" * (len(middle_rib) - 2)
        table_bottom = "#" + table_lenght + "#"
        table_top = "#" + table_lenght + "#"

        resoult = table_top + "\n" + table_element[:-(len(middle_rib)+2)] + "\n" + table_bottom + "\n"
        return resoult
