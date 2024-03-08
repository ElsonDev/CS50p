# function to take user intput and call function emotechange #
def main():
    userinput = input()
    emotechange(userinput)

# define emotechange function to replace userinput str #
def emotechange(str):
    newstring = str.replace(":)", "\U0001F642") .replace(":(", "\U0001F641")
    print(newstring)

main()