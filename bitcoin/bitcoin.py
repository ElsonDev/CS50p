import requests
import sys


# Output the current cost of 'x' Bitcoins in USD to four decimal places, using ',' as a thousands separator.

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command line argument")
    else:
        amount = float(sys.argv[1])

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()

    usd_bitcoin = o["bpi"]["USD"]["rate_float"]
    usd_bitcoin = float(usd_bitcoin)
    total_bitcoins = usd_bitcoin * amount
    total_bitcoins = round(total_bitcoins, 4)
    print(f"${total_bitcoins:,}")



except requests.RequestException:
    pass

except ValueError:
    sys.exit("Command-line argument not a number")
