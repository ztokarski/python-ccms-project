from user import *


class Open:

    def open_users(self, user_list):
        users_list = []
        read_file = open(user_list, "r")
        for user in read_file:
            users_list.append(user.strip().split(","))
            read_file.close()
        return list(users_list)

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
        middle_rib = ("|" + "-" * 19) * 5 + "|"
        for object in object_list:
            element = "|   " + object.name
            while len(element) < 20:
                element += " "
            element1 = "|   " + object.surname
            while len(element1) < 20:
                element1 += " "
            element2 =  "|   " + object.login
            while len(element2) < 20:
                element2 += " "
            element3 = "|   " + object.password
            while len(element3) < 20:
                element3 += " "
            element4 = "|   " + object.state
            while len(element4) < 20:
                element4 += " "
            table_element += element + element1 + element2 + element3 + element4 + "|" + "\n" + middle_rib + "\n"

        # Frames
        table_lenght = "-" * 99
        table_bottom = "#" + table_lenght + "#"
        table_top = "#" + table_lenght + "#"

        resoult = table_top + "\n" + table_element[:-(len(middle_rib)+2)] + "\n" + table_bottom + "\n"
        return resoult
