def main():
    greeting = input("Greeting: ")
    print("$",value(greeting), sep = "")

def value(greeting):
    greeting = greeting.lower().strip()

    if greeting.startswith("hello"):
        return 20
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()