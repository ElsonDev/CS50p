# Price list currency converter
## Video Demo:  <https://www.youtube.com/watch?v=xX8bLdMFWU4>
## About the Project
I have developed a program to convert an imported price list from its base currency to another supported currency and export it as CSV.

I designed this program to improve the speed, efficiency and accuracy of converting a spreadsheet of prices used by my place of work from the base currency, which happens to be GBP to other currencies supported by the business.

This program takes a price list in csv format as input, uses an API request to get the latest currency exchange rate for the base rate and selected conversion currency and converts the file from the base currency to the conversion currency and exports a corresponding csv file into the export folder.

In this project I used a small subset of pricing data as a proof of concept, with a view of further developing this program to handle more complex pricing data which is ultimatley where this program will be most effective to business operations.

## Usage

The program takes two command line arguments.

1. File location + filename

    The program accepts a file located anywhere on the users system and the file must be in '.CSV' format.

    The filename also needs to be suffixed at the end of the filename with the files current currency using the 3 digit code in ISO 4217 format and supported by the program (see 'supported_currencies.csv'), and is case-insensitive, for example:

        .../price_master_GBP.csv
        .../price-master-gbp.csv
        .../priceMasterGBP.csv

2. Conversion currency

    The program accepts any currency code listed in the 'supported_currencies.csv' for example:

        USD
        EUR
        AUD


## Functions
### is_valid
This function takes the command line input from the user and checks to ensure a file in '.CSV' format and conversion currency is provided.

### supported_currency
This function takes the currency code provided by the user and checks it against the list of supported currnecies listed in 'supported_currencies.csv'.

### get_base
This function takes checks the existing currency of the file provided by the user and checks to ensure this currency is supported by checking the currencies listed in 'supported_currencies.csv'.

### get_rate
The get_rate function takes the existing currency of the file and the conversion currency provided by the user and makes an API request to <http://api.freecurrencyapi.com> to get the latest exchange rate of the base currency and the conversion currency.

### convert_csv
This function then converts the file provided by the user from the base currency to the conversion currency using the latest exchange rate and creates a corresponding '.CSV' file in the export folder 

## License
Distributed under the MIT License.

## Contact
Steven Elson - https://github.com/ElsonDev




