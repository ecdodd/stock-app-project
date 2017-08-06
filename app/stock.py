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
