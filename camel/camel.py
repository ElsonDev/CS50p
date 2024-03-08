def main():
    og_name = input("camelCase: ")
    snake_converter(og_name)

def snake_converter(camelstring):
    print("snake_case: ", end="")

    for i in camelstring:
        if i.islower():
            print(i, end="")
        else:
            print("_" + i.lower(), end="")
    print()

main()