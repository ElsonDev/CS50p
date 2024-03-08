import requests, sys, csv
from os import path

API_KEY = "fca_live_1qk6O57lirDgD9mubp5HsnMY53RYXTUsQVtWLXxe"

def main():
    if is_valid(sys.argv):
        export_currency, export_symbol = supported_currency(sys.argv[2])
        base_rate, base_symbol = get_base(sys.argv[1])
        exchange_rate = get_rate(base_rate, export_currency)
        convert_csv(sys.argv[1], base_symbol, export_currency, export_symbol, exchange_rate)

# validate the users input through cli. *upgrade this function to use argparser in future version*
def is_valid(cli):
    if len(cli[1:]) != 2:
        sys.exit("ERROR: Expecting two arguments, a .csv file, and conversion currency code, e.g. 'USD'.")
    root_ext = path.splitext(cli[1])
    if root_ext[1] != ".csv":
        sys.exit(f"ERROR: '{root_ext[1]}' is not a valid file format, expecting file in '.csv' format.")
    elif len(cli[2]) != 3:
        sys.exit(f"ERROR: '{cli[2]}' is not a valid currency code.")
    return True

# get the required currency from the user and check to ensure currency code is supported by the API by way of a CSV file
def supported_currency(code):
    try:
        with open("supported_currencies.csv", "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if code.upper() == row["Code"]:
                    return row["Code"], row["Symbol"]
            else:
                sys.exit(f"ERROR: '{code}' is not supported, try an alternative.")

    except FileNotFoundError:
        sys.exit("supported_currencies.csv not found.")

# get the base currency to convert from if supported by the API
def get_base(file):
    root_ext = path.splitext(file)
    root = root_ext[0]
    root = root.upper()
    try:
        with open("supported_currencies.csv", "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if root.endswith(row["Code"]):
                    return row["Code"], row["Symbol"]
            else:
                sys.exit(f"Base currency not supported.")

    except FileNotFoundError:
        sys.exit("supported_currencies.csv not found.")

# get the latest exchange rate of the base currency (import) and the conversion currency (export) via API
def get_rate(base_cur, conversion_cur):
    resp = requests.get(f"http://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}&currencies={conversion_cur}&base_currency={base_cur}")
    o = resp.json()
    exchange_rate = o["data"][conversion_cur]
    return exchange_rate


# import csv price list provided by user, convert to conversion currency and export to csv
def convert_csv(file, base_symbol, export_currency, export_symbol, exchange_rate):
    prices = []
    try:
        with open(file, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                nfc = row["NFC"].strip(base_symbol)
                nfc = float(nfc)
                nfc = nfc * exchange_rate
                nfc = round(nfc, 2)
                nfc = f"{export_symbol}{nfc:.2f}"

                non_nfc = row["Non-NFC"].strip(base_symbol)
                non_nfc = float(non_nfc)
                non_nfc = non_nfc * exchange_rate
                non_nfc = round(non_nfc, 2)
                non_nfc = f"{export_symbol}{non_nfc:.2f}"

                qty = row["Quantity"]

                prices.append({"NFC": nfc, "Non-NFC": non_nfc, "Quantity": qty})

        with open(f"export/export_{export_currency}.csv", "w") as newf:
            fieldnames =["NFC", "Non-NFC", "Quantity"]
            writer = csv.DictWriter(newf, fieldnames)
            writer.writeheader()
            for price in prices:
                writer.writerow(price)
    except FileNotFoundError:
        sys.exit(f"'{file}' not found.")




if __name__ == "__main__":
    main()
