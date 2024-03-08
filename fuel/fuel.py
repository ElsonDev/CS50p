def main():
    while True:
        try:
            prompt = input("Fraction: ")

            #split input, assign input as X and Y spliting at /
            x, y = prompt.split("/")
            #convert X and Y to ints
            x = int(x)
            y = int(y)

            percent = round((100 * x) / y)

            if percent <= 1:
                print("E")
            elif percent >= 99 and percent <= 100:
                print("F")
            elif x > y or y == 0:
                raise ValueError
            else:
                print(percent,"%", sep="")

#If, though, X or Y is not an integer
# X is greater than Y,
# or Y is 0 instead prompt the user again. (It is not necessary for Y to be 4.)




        except ZeroDivisionError:
            pass

        except ValueError:
            pass


        else:
            break



main()

