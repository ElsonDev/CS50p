import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})






"""
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
"""