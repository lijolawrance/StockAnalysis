import time

import pandas as pd

from notebooks.Database import Database


class StockData:
    def __init__(self):
        self.df_stock_data = pd.DataFrame()

    def load_data_from_yFinance(self, stock, period, interval):
        self.df_stock_data = stock.history(period=period, interval=interval, )

    def drop_columns_frm_df(self, **kwargs):
        [self.df_stock_data.drop(value, axis='columns', inplace=True) for key, value in kwargs.items()]

    def load_data_to_sqllite(self, stock_name):
        db = Database()
        #self.df_stock_data['load_time'] = time.localtime()
        db.load_file(self.df_stock_data, stock_name)

    def write_data_to_csv(self, stock_name):
        self.df_stock_data.to_csv('data/' + stock_name + '.csv')

    def get_dataFrame(self):
        return self.df_stock_data
