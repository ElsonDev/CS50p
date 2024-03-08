import emoji


def main():

    userinput = input("Input: ").strip()

    print(emoji.emojize(userinput, language='alias'))
















if __name__ == "__main__":
    main()