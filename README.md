# THE STOCK APPLICATION

This app allows users to input a stock symbol and returns the stock prices for the last 15 days (non-trading days excluded). These include the prices for Open, High, Low, and Close, as well as the Volume.

## INSTALLATION

This application was designed using Python 3.6.1. Users must have Python version (3.x) installed to run this app.

Download the source code:

```shell
git clone https://github.com/ecdodd/stock_app
cd desktop/stock_app/
```

Install package dependencies:

'''shell
pip3 install pandas-datareader
'''

Finally, create a csv file entitled stocks.csv and and save it as `data/stocks.csv`. Add the following headers to file: 'Date', 'Symbol', 'Open', 'High', 'Low', 'Close', 'Volume'.  

## USAGE

```shell
python3 app/stock.py
```

You must re-run the shell for each new operation (either 'display' or 'add') you wish to run.
