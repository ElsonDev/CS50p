# name = input("What's your name? ")
# file.write(f"{name}\n")

names = []

for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"hello, {name}")


            for line in ogf:
                if "name,house" in line:
                     continue
                line = line.replace('"','')
                line = line.strip()
                last, first, house = line.split(',')

                students.append({"last": last, "first": first, "house": house})
                print(line)



                sorted(students, key=lambda student: student["first"]):