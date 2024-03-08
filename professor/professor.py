from random import randint
import sys


def main():
    total_score = 0
    incorrect_answers = 0
    problem_number = 1

    # ten math problems
    # if answer is correct then tally score
    # if wrong answer provided print EEE
    # if wrong answer provided 3 times output corrrect answer and generate new math problem

    try:
        level = get_level()

        # loop below until 10 math problems generated
        while problem_number <= 10:
            x, y = generate_integer(level)
            actual_answer = x + y

            # loop below until 3 incorrect answer provided
            while incorrect_answers < 3:
                user_answer = input(f"{x} + {y} = ")

                if user_answer.isdigit():
                    user_answer = int(user_answer)
                    if actual_answer == user_answer:
                        total_score += 1
                        problem_number += 1
                        break
                    else:
                        incorrect_answers += 1
                        print("EEE")
                        continue

                else:
                    incorrect_answers += 1
                    print("EEE")
                    continue

            if incorrect_answers == 3:
                print(f"{x} + {y} = ", actual_answer)
                incorrect_answers = 0
                problem_number += 1
                continue

        print("Score: ", total_score)
        sys.exit()

    except ValueError:
        pass


def get_level():
    # promtps user for level and repromps if required
    # level 1 2 or 3
    while True:
        user_level = input("Level: ")

        if user_level.isdigit():
            user_level = int(user_level)

            if user_level >= 1 and user_level <= 3:
                return user_level

            else:
                pass

        else:
            continue


def generate_integer(level):
    if level == 1:
        x = randint(0, 9)
        y = randint(0, 9)
    elif level == 2:
        x = randint(10, 99)
        y = randint(10, 99)
    elif level == 3:
        x = randint(100, 999)
        y = randint(100, 999)
    else:
        raise ValueError

    return (x, y)


if __name__ == "__main__":
    main()
