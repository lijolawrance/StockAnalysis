from notebooks import StockData, Utilities
import pandas as pd
import yfinance as yahoo
import re

regex = '[^A-Za-z0-9]+'
sd = StockData.StockData()
ut = Utilities.Utilities()

# stock = yahoo.tickers.multi.download(['SBIN.NS', 'HDFCBANK.NS'], start='1-1-2018')
stock = yahoo.Ticker('SBIN.NS')

file_name = re.sub(regex, '', stock.info['longName'])
sd.load_data_from_yFinance(stock, '5y', '1d')
sd.drop_columns_frm_df(first='Dividends', second='Stock Splits')
print(sd.get_dataFrame().columns)
# sd.write_data_to_csv(file_name)
#ut.merge_dataFrame(first=sd.get_dataFrame(), second=sd.get_dataFrame())
#var2 = ut.get_dataFrame()
#print(var2)
