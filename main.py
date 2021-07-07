from notebooks import StockData, Utilities
import pandas as pd
import yfinance as yahoo
import re

regex = '[^A-Za-z0-9]+'


class Main:

    def __init__(self, symbol):
        self.stock = yahoo.Ticker(symbol)
        self.stock_name = re.sub(regex, '', self.stock.info['shortName'])
        self.sd = StockData.StockData()
        self.ut = Utilities.Utilities()

    def get_stock_name(self):
        return self.stock, self.stock_name

    def load_stock_details(self):
        self.sd.load_data_from_yFinance(self.stock, '5y', '1d')
        self.sd.drop_columns_frm_df(first='Dividends', second='Stock Splits')
        self.sd.load_data_to_sqllite(self.stock_name)

    def gen_stock_for_analysis(self):
        self.sd.load_data_from_yFinance(self.stock, '5y', '1d')
        self.sd.drop_columns_frm_df(first='Dividends', second='Stock Splits')
        self.sd.load_data_to_sqllite(self.stock_name)


Main('ICICIBANK.NS').load_stock_details()
Main('SBIN.NS').load_stock_details()
Main('HDFCBANK.NS').load_stock_details()
#main.load_stock_details()

# stock = yahoo.tickers.multi.download(['SBIN.NS', 'HDFCBANK.NS'], start='1-1-2018')

# sd.write_data_to_csv(file_name)
# ut.merge_dataFrame(first=sd.get_dataFrame(), second=sd.get_dataFrame())
# var2 = ut.get_dataFrame()
# print(var2)
