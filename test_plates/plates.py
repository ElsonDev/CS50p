def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    x = False
    numinplate = False
    zeroinplate = False

    # First number used in string cannot be 0
    # numbers must come at the end of a string

    # checking each char of string
    for c in s:
        # if char is a digit then run code below
        if c.isdigit():
            x = True
            # if digit is 0 then intitialise variable zeropos with index position of 0 in the string
            if c == "0":
                zeropos = s.index("0")
                zeroinplate = True
            # if digit is not 0 then intitialise variable numpos with index position of the digit in the string
            else:
                numpos = s.index(c)
                numinplate = True
        # if c is not a digit loop until it is
        else:
            continue

    while x == True:
        if numinplate == True and zeroinplate == True:
            if numpos < zeropos and s[numpos:len(s)].isdigit() and s.isalnum():
                return True
            else:
                return False

        if numinplate == True and zeroinplate == False:
            if s[numpos:len(s)].isdigit() and s.isalnum():
                return True
            else:
                return False

    if s[0:2].isalpha() and len(s) >=2 and len(s) <=6 and s.isalnum():
        return True
    else:
        return False



if __name__ == "__main__":
    main()