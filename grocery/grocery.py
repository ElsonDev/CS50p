def main():

#try dictionary instead with product key and qty value
#if product is entered and exists increase qty by 1
# user gives input, input added to a list and then print the list and count each item
    allgroceries = []
    noduplicates = []

    while True:
        try:
            product = input().strip().upper()
            allgroceries.append(product)
            allgroceries.sort()
            if allgroceries.count(product) == 1:
                noduplicates.append(product)
                noduplicates.sort()
            else:
                continue

        except EOFError:
            for fruit in noduplicates:
                print(allgroceries.count(fruit), fruit)
            break


main()