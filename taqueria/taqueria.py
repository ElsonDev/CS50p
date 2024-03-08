def main():

    menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    totalprice = float(0.00)
    price = float(0.00)

    while True:
        try:
            prompt = input("Item: ").strip()
            selecteditem = prompt.title()
            for food in menu:
                if food == selecteditem:
                    price = menu[selecteditem]
                    totalprice = totalprice + price
                    print(f"Total: ${totalprice:.2f}", sep="")
                else:
                    continue
        except (SyntaxError, KeyError):
            pass
        except EOFError:
            print()
            break




main()
