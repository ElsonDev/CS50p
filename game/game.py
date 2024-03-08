from random import randint
import sys

def main():

    while True:
        try:
            levelselect = input("Level: ")
            levelselect = int(levelselect)
            guess = 0
            if levelselect < 1:
                 continue

            else:
                answer = randint(1, levelselect)

            while guess != answer:
                guess = input("Guess: ")
                if guess.isdigit():
                    guess = int(guess)
                    if guess > answer:
                        print("Too large!")
                        continue
                    elif guess < answer:
                        print("Too small!")
                        continue
                    else:
                        print("Just right!")
                        sys.exit()
                else:
                    continue




        except ValueError:
            pass
















if __name__ == "__main__":
    main()
