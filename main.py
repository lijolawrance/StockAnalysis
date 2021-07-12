from notebooks import StockData, Utilities, Database
import pandas as pd
import yfinance as yahoo
import re

from notebooks.QtPandas import display_dataframe

regex = '[^A-Za-z0-9]+'


class Main:

    def __init__(self, symbol):
        self.stock = yahoo.Ticker(symbol)
        print(self.stock)
        self.stock_name = re.sub(regex, '', self.stock.info['shortName'])
        self.sd = StockData.StockData()

    def get_stock_name(self):
        return self.stock, self.stock_name

    def load_stock_details(self):
        self.sd.load_data_from_yFinance(self.stock, '5y', '1d')
        self.sd.drop_columns_frm_df(first='Dividends', second='Stock Splits')
        self.sd.load_data_to_sqllite(self.stock_name)
        return self.sd.get_dataFrame()


ut = Utilities.Utilities()
Main('SBIN.NS').load_stock_details()
Main('HDFCBANK.NS').load_stock_details()
Main('^NSEI').load_stock_details()
Main('ICICIBANK.NS').load_stock_details()
query = 'select n.date,n.close as NIFTY,s.close as SBI ,h.close as HDFC, i.close ' \
        'as ICICI from HDFCBANK h, NIFTY50 n,STATEBKOFINDIA s, ICICIBANK i where ' \
        'h.Date=n.Date and n.Date=s.Date and h.Date=s.Date and i.Date=n.Date'
display_dataframe(ut.fetch_data_for_analysis(query))
# main.load_stock_details()

# stock = yahoo.tickers.multi.download(['SBIN.NS', 'HDFCBANK.NS'], start='1-1-2018')

# sd.write_data_to_csv(file_name)
# ut.merge_dataFrame(first=sd.get_dataFrame(), second=sd.get_dataFrame())
# var2 = ut.get_dataFrame()
# print(var2)
