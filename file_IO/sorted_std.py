# This script reads student data from a CSV file, sorts it by student names,
# and writes the sorted data to a new CSV file.

import csv

students = []

# read all rows
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if row:  # skip empty lines
            students.append(row)

# sort by first column (name)
students.sort(key=lambda x: x[0])

# write sorted data
with open("sorted_students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", " school"])
    writer = csv.writer(file)
    writer.writerows(students)


students.sort(key=lambda x: x[0])
print()
print("Here is the List of Sorted Students")
print("********")

for student in students:
    name, school = student
    print(f"{name}, is in {school}")

print()
print("****END OF FILE****")
print()
