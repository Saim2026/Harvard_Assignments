# This program will add names to students.py and save them to a CSV file.

import csv  # import the csv module, pip install if necessary


def main():
    name = input("Enter your name: ")
    school = input("Enter your school: ")

    with open("students.csv", "a") as students:
        writer = csv.DictWriter(students, fieldnames=["name", "school"])
        # writer.writeheader()

        writer.writerow({"name": name, "school": school})
    students.close()


main()
print("**** Thank you for the information! ****")
