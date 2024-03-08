def main():

    time = input("What time is it? ")

    if convert(time) >= 7.0 and convert(time) <= 8.0:
        print("breakfast time")

    elif convert(time) >= 12.0 and convert(time) <= 13.0:
        print("lunch time")

    elif convert(time) >= 18.0 and convert(time) <= 19.0:
        print("dinner time")


def convert(time):
    # convert time from string to float to corresponding number of hours in 24 hour clock
    # seperator :
    # keep first whole hours
    # then convert minutes to fraction /60
    # then add them back together

    hour, minute = time.split(":")
    mintofrac = float(minute) / 60
    hour = float(hour)
    time = hour + mintofrac

    return float(time)



if __name__ == "__main__":
    main()