import pandas as pd
from notebooks.Database import Database


class Utilities:
    def __init__(self):
        self.db = Database()
        self.df_utility = pd.DataFrame()

    def merge_dataFrame(self, **kwargs):
        for key, value in kwargs.items():
            # print(value.head(2))
            self.df_utility.append(value, ignore_index=False)
            print(self.df_utility.head(2))

    def get_dataFrame(self):
        return self.df_utility

    def fetch_data_for_analysis(self, sql_query):
        return self.db.fetch_data(sql_query)
