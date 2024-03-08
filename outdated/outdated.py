def main():
    # I could print the index position of the list of months
    # if prefix of string contains item in list do x else do y

    x = True
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    while x == True:
        try:
            odate = input("Date: ").strip()

            for month in months:
                if odate.startswith(month):
                    if valid_longform(odate):
                        mm, dd, yyyy = odate.split(" ")
                        month_number = months.index(mm) + 1
                        month_number = str(month_number)
                        month_number = month_number.zfill(2)
                        dd = dd.strip(",")
                        dd = dd.zfill(2)
                        yyyy = yyyy.strip(" ")
                        yyyy = yyyy.zfill(4)
                        print(f"{yyyy}-{month_number}-{dd}")
                        x = False
                    else:
                        break
                else:
                    continue

            if valid_shortform(odate):
                mm, dd, yyyy = odate.split("/")
                mm = mm.zfill(2)
                dd = dd.zfill(2)
                yyyy = yyyy.zfill(4)
                print(f"{yyyy}-{mm}-{dd}")
                x = False
            else:
                continue























        except ValueError:
            pass




def valid_longform(date):
    month, day, year = date.split(" ")
    if day.isdigit():
        return False
    day = day.strip(",")
    day = int(day)
    year = year.strip(" ")
    year = int(year)

    # check days
    if day < 1 or day > 31:
        return False
    # check year
    elif year < 1 or year > 9999:
        return False
    else:
        return True

def valid_shortform(date):
    month, day, year = date.split("/")
    month = int(month)
    day = int(day)
    year = int(year)

    # check months
    if month < 1 or month > 12:
        return False
    # check day
    if day < 1 or day > 31:
        return False
    # check year
    elif year < 1 or year > 9999:
        return False
    else:
        return True


main()



