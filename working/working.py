import re
import sys

# 9:00 AM to 5:00 PM
# 9 AM to 5 PM

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^([0-9]|1[0-2])(?:\:([0-5][0-9]))? (AM|PM) to ([0-9]|1[0-2])(?:\:([0-5][0-9]))? (AM|PM)$", s):
        start_hour = matches.group(1)
        start_minute = matches.group(2)
        start_meridian = matches.group(3)
        end_hour = matches.group(4)
        end_minute = matches.group(5)
        end_meridian = matches.group(6)

        if start_meridian == "AM":
            if start_hour == "12":
                start_hour = "00"
            elif len(start_hour) == 1:
                start_hour = "0" + start_hour

        if start_meridian == "PM":
            start_hour = int(start_hour)
            if start_hour <= 11:
                start_hour = start_hour + 12

        if end_meridian == "AM":
            if end_hour == "12":
                end_hour = "00"
            elif len(end_hour) == 1:
                end_hour = "0" + end_hour

        if end_meridian == "PM":
            end_hour = int(end_hour)
            if end_hour <= 11:
                end_hour = end_hour + 12

        if start_minute == None:
            start_minute = "00"

        if end_minute == None:
            end_minute = "00"

        return f"{start_hour}:{start_minute} to {end_hour}:{end_minute}"

    else:
        raise ValueError

if __name__ == "__main__":
    main()