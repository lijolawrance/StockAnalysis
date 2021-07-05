import pandas as pd


class Utilities:
    def __init__(self):
        self.df_utility = pd.DataFrame()

    def merge_dataFrame(self, **kwargs):
        for key, value in kwargs.items():
            # print(value.head(2))
            self.df_utility.append(value, ignore_index=False)
            print(self.df_utility.head(2))

    def get_dataFrame(self):
        return self.df_utility
