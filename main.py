from notebooks import StockData, Utilities
import pandas as pd
import yfinance as yahoo
import re

regex = '[^A-Za-z0-9]+'
sd = StockData.StockData()
ut = Utilities.Utilities()
stock = yahoo.Ticker("AMZN")
file_name = re.sub(regex, '', stock.info['longName'])
sd.load_data_from_yFinance(stock, 'max', '1d')
# sd.write_data_to_csv(file_name)
ut.merge_dataFrame(first=sd.get_dataFrame(), second=sd.get_dataFrame())
var2 = ut.get_dataFrame()
#print(var2)
