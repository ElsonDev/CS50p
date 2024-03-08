def vend_machine():
    coin_total = 0
    amount_due = 50
    print("Amount Due:", amount_due)

    while coin_total < 50 :
        coins = int(input("Insert coin: "))

        if coins == 25:
            coin_total += 25

            if coin_total < 50:
                print("Amount Due:", 50 - coin_total)

            else:
                continue

        elif coins == 10:
            coin_total += 10

            if coin_total < 50:
                print("Amount Due:", 50 - coin_total)

            else:
                continue

        elif coins == 5:
            coin_total += 5

            if coin_total < 50:
                print("Amount Due:", 50 - coin_total)

            else:
                continue
        else:
            print("Amount Due:", 50 - coin_total)


    print("Change Owed:", coin_total - 50)


vend_machine()