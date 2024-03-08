import csv
import sys
from tabulate import tabulate

def main():
      if isvalid(sys.argv):
        print(makepretty(sys.argv[1]))

def isvalid(cli):
    if len(cli) < 2:
            sys.exit("Too few command-line arguments")
    elif len(cli) > 2:
            sys.exit("Too many command-line arguments")
    elif cli[1].endswith(".csv"):
            return True
    else:
         sys.exit("Not a CSV file")

def makepretty(file):
    with open(file) as f:
        table = csv.reader(f)
        return tabulate(table, headers="firstrow", tablefmt="grid")


if __name__ == "__main__":
    main()