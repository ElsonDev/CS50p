from datetime import date, timedelta
import sys
import inflect

p = inflect.engine()

def main():
    print(convert(input("Date of Birth: ")))


def convert(bd):
    try:
        today = date.today()
        birthday = date.fromisoformat(bd)
        minute = timedelta(seconds=60)
        days = today - birthday
        age_in_mins = days / minute
        age_in_mins = round(age_in_mins)
        words = p.number_to_words(age_in_mins, andword="")

        return words.capitalize() + " minutes"

    except ValueError:
        sys.exit(ValueError)


if __name__ == "__main__":
    main()
