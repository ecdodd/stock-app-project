import csv
from pandas_datareader import data
from datetime import date, timedelta
from IPython import embed

# READ STOCKS CSV

stocks = []

csv_file_path = "data/stocks.csv"

# DISPLAY MENU #1

stock_menu = """
------------------------------------------------------
    STOCK APPLICATION
------------------------------------------------------
    Welcome to the stock app!

    Enter stock symbol: """

stock_symbol = input(stock_menu)
symbol = stock_symbol

# DISPLAY MENU #2

operation_menu = """

    Operation | Description
    --------- |-------------
    'display' | Display a range of stock values.
    'add'     | Add a range of stock values to a file.

    Enter operation: """

input_operation = input(operation_menu)
operation = input_operation.lower()

# COMPILE REQUEST PARAMETERS

data_source = 'google'
start = str(date.today() - timedelta(days=15))
end = str(date.today())
response = data.DataReader(symbol, data_source, start, end)

# DEFINE FUNCTIONS

def display_stocks(response):
    response["Symbol"] = symbol
    columns = ["Symbol", "Open", "High", "Low", "Close", "Volume"]
    response = response[columns]
    print(response)
    print("Source: " + (data_source))

def add_stocks(response):
    response["Symbol"] = symbol
    columns = ["Symbol", "Open", "High", "Low", "Close", "Volume"]
    response = response[columns]
    response.to_csv(csv_file_path, mode = 'a', header=False)
    print("Thank you! Your response has been saved.")

# CONTROL FLOW

if operation == "display": display_stocks(response)
elif operation == "add": add_stocks(response)
else: print("Error. Please choose one of the recognized operations.")
