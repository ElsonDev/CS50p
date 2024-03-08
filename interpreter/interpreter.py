def main():
    # prompt the user for input #
    # split user input into 3 parts and convert from string to float where required

    expression = input("Expression: ")

    x, y, z = expression.split(" ")

    x = float(x)
    z = float(z)

    if y == "+":
        answer = x + z
        print (float(answer))
    elif y == "-":
        answer = x - z
        print (float(answer))
    elif y == "/":
        answer = x / z
        print (float(answer))
    elif y == "*":
        answer = x * z
        print (float(answer))
    else:
        print("Unknown Operator")



main()
