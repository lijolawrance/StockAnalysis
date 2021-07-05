import pandas as pd


class StockData:
    def __init__(self):
        self.df_stock_data = pd.DataFrame()

    def load_data_from_yFinance(self, stock, period, interval):
        self.df_stock_data = stock.history(period=period, interval=interval)

    def drop_columns_frm_df(self, column):
        self.df_stock_data.drop([column])

    def write_data_to_csv(self, stock_name):
        self.df_stock_data.to_csv('data/' + stock_name + '.csv')

    def get_dataFrame(self):
        return self.df_stock_data
