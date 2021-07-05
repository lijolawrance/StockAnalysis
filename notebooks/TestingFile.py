import yfinance as yf
import pandas as pd
share = yf.Ticker("SBIN.NS")
company = share.info['longName']
print(share.info)
df = pd.DataFrame()
df=share.history(period="1mo", interval="1d" )
print(df.columns)
print(df.head(5))