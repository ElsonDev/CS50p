def main():
    while True:
        try:
            prompt = input("Fraction: ")
            print(gauge(convert(prompt)))

        except ZeroDivisionError:
            pass

        except ValueError:
            pass

        else:
            break

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError()
    elif x > y:
        raise ValueError()
    else:
        percent = round((100 * x) / y)
        return percent

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99 and percentage <= 100:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()