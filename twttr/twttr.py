def main():
    mytwt = input("What do you want to say? ")
    onlycont(mytwt)

def onlycont(words):


    for i in words:
        if i == "A" or i == "E" or i == "I" or i == "O" or i ==  "U" or i ==  "a" or i ==  "e" or i ==  "i" or i ==  "o" or i == "u":
            print("", end="")
        else:
            print(i, end="")

    print()








main()