import csv
import sys

students = []

def main():
    if isvalid(sys.argv):
        convert(sys.argv[1], sys.argv[2])

def isvalid(cli):
    if len(cli[1:]) < 2:
            sys.exit("Too few command-line arguments")
    elif len(cli[1:]) > 2:
            sys.exit("Too many command-line arguments")
    elif cli[1].endswith(".csv") and cli[2].endswith(".csv"):
            return True
    else:
         sys.exit("Not CSV files")


def convert(file1, file2):
    try:
        with open(file1, "r", newline="") as ogf:
            reader = csv.DictReader(ogf)
            for row in reader:
                 last, first = row["name"].split(",")
                 house = row["house"]
                 first = first.strip()
                 last = last.strip()
                 students.append({"first": first, "last": last, "house": house})

        with open(file2, "w") as newf:
            fieldnames=["first", "last", "house"]
            writer = csv.DictWriter(newf, fieldnames=fieldnames)
            writer.writeheader()
            for student in students:
                writer.writerow(student)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

if __name__ == "__main__":
    main()
