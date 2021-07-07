from notebooks import StockData, Utilities
import pandas as pd
import yfinance as yahoo
import re

regex = '[^A-Za-z0-9]+'


class Main:

    def __init__(self):
        self.sd = StockData.StockData()
        self.ut = Utilities.Utilities()

    def load_stock_details(self, stock, stock_name):
        self.sd.load_data_from_yFinance(stock_name, '5y', '1d')
        self.sd.drop_columns_frm_df(first='Dividends', second='Stock Splits')
        self.sd.load_data_to_sqllite(stock_name)

    def gen_stock_for_analysis(self, stock, stock_name):
        self.sd.load_data_from_yFinance(stock, '5y', '1d')
        self.sd.drop_columns_frm_df(first='Dividends', second='Stock Splits')
        self.sd.load_data_to_sqllite(stock_name)


def get_stock_name(stock_symbol):
    stock = yahoo.Ticker(stock_symbol)
    stock_name = re.sub(regex, '', stock.info['shortName'])
    return stock, stock_name


main = Main()
main.load_stock_details('^NSEI')
main.load_stock_details('SBIN.NS')
main.load_stock_details('HDFCBANK.NS')
stock, stock_name = get_stock_name('ICICIBANK.NS')
main.load_stock_details(stock, stock_name)

# stock = yahoo.tickers.multi.download(['SBIN.NS', 'HDFCBANK.NS'], start='1-1-2018')

# sd.write_data_to_csv(file_name)
# ut.merge_dataFrame(first=sd.get_dataFrame(), second=sd.get_dataFrame())
# var2 = ut.get_dataFrame()
# print(var2)
