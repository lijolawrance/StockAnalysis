import sqlite3
import pandas as pd


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('C:/databases/stock.db')

    def load_file_excel(self):
        df_excel = pd.DataFrame()
        df_excel = pd.read_excel('C:/Users/lijol/Downloads/Yahoo Ticker Symbols - September 2017.xlsx',
                                 sheet_name='Stock')
        df_excel.to_sql(con=self.conn, name='yahoo_tickers')

    def load_file(self, df_stock, stock_name):
        df_stock.to_sql(con=self.conn, name=stock_name, if_exists='replace')

