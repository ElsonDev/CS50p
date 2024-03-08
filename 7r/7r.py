import sys, csv, os

def main():
    sevenrooms = []
    clients = []
    matches = 0
    with open("7r.csv", "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sevenrooms.append(row)
    with open("clients.csv", "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            clients.append(row)


    for row in sevenrooms:
         for row in clients:
            print(row)
            if row["website"] == sevenrooms[0]:
                matches += 1

    print(matches)










if __name__ == "__main__":
    main()
