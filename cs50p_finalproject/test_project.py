import pytest
from project import is_valid, supported_currency, get_base, get_rate, convert_csv
import requests
import os

def test_is_valid():
    cli = ["project.py", "import/price_master_gbp.csv", "USD"]
    assert is_valid(cli) == True
    with pytest.raises(SystemExit):
        cli = ["project.py", "import/price_master_gbp.jpg", "USD"]
        is_valid(cli)
        cli = ["project.py", "import/price_master_gbp.csv", "USDD"]
        is_valid(cli)

def test_supported_currency():
    assert supported_currency("USD") == ("USD", "$")
    assert supported_currency("gbp") == ("GBP", "£")
    with pytest.raises(SystemExit):
        supported_currency("ABC")

def test_get_base():
    file = "import/price_master_gbp.csv"
    assert get_base(file) == ("GBP", "£")
    file = "import/price_master_USD.csv"
    assert get_base(file) == ("USD", "$")
    file = "import/price_master_ABC.csv"
    with pytest.raises(SystemExit):
        get_base(file)

def test_get_rate():
    url = "http://api.freecurrencyapi.com/v1/latest?apikey=fca_live_1qk6O57lirDgD9mubp5HsnMY53RYXTUsQVtWLXxe&currencies=USD&base_currency=GBP"
    resp = requests.get(url)
    assert resp.status_code == 200

def test_convert_csv():
     file = "import/price_master_gbp.csv"
     base_symbol = "£"
     export_currency = "USD"
     export_symbol = "$"
     exchange_rate = 1.2375163795
     convert_csv(file, base_symbol, export_currency, export_symbol, exchange_rate)
     assert os.path.exists("export/export_USD.csv")


