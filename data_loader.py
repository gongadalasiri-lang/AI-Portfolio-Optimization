import yfinance as yf
import pandas as pd

def get_data():
    stocks = ['RELIANCE.NS', 'TCS.NS', 'INFY.NS', 'HDFCBANK.NS']
    data = yf.download(stocks, start="2020-01-01", end="2024-01-01")['Close']
    returns = data.pct_change().dropna()
    return data, returns