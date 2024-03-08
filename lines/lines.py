import sys

def main():
    if isvalid(sys.argv):
        print(linecount(sys.argv[1]))

def isvalid(cli):
    if len(cli) < 2:
            sys.exit("Too few command-line arguments")
    elif len(cli) > 2:
            sys.exit("Too many command-line arguments")
    elif cli[1].endswith(".py"):
            return True
    else:
         sys.exit("Not a Python file")

def linecount(file):
    # exclude blank (whitespace) lines
    # exclude comments
    clines = 0
    try:
        with open(file) as f:
            for line in f:
                if line.lstrip().startswith("#"):
                    pass
                elif line.isspace():
                    pass
                else:
                    clines += 1
        return clines

    except FileNotFoundError:
         sys.exit("File not found!")












if __name__ == "__main__":
    main()