import inflect
import sys

def main():

    p = inflect.engine()
    namelist = []


    while True:
        try:
            user_input = input("Name: ")
            namelist.append(user_input)


        except EOFError:
            mylist = p.join((namelist))
            print("Adieu, adieu, to", mylist)
            sys.exit()













if __name__ == "__main__":
    main()