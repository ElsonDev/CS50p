def main():
    userinput = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
    if userinput == "42" or userinput == "forty two" or userinput == "forty-two":
        print("Yes")
    else:
        print("No")

main()



