import validators

def main():
    email = input("What's your email address? ")
    if is_valid(email):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return validators.email(s)


if __name__ == "__main__":
    main()