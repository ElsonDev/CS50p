from pyfiglet import Figlet
from random import choice
import sys






def main():
    f = Figlet()
    figlet_fonts = f.getFonts()
    accepted_arg = ["-f", "--font"]


    try:
        if len(sys.argv) < 2:
            f.setFont(font=choice(figlet_fonts))
        elif sys.argv[1] not in accepted_arg:
                sys.exit("Not the correct argument")
        elif sys.argv[2] not in figlet_fonts:
                sys.exit("Not a valid font")
        else:
            f.setFont(font=sys.argv[2])

        userinput = input("Input: ")
        print(f.renderText(userinput))




    except IndexError:
        pass




























if __name__ == "__main__":
    main()
