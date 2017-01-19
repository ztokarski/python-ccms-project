import csv


def create_card(name, surname):
    file_name = str(name + surname + ".csv")
    with open(file_name, "w") as csvfile:
        januszwriter = csv.writer(csvfile)
        januszwriter.writerow(["Student"])
        januszwriter.writerow([name, surname])
        januszwriter.writerow(["Assigments"])
