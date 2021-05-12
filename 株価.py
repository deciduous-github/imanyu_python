import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

aapl = yf.Ticker('AAPL')

day = 20
print(aapl.history(period=f'{day}d'))
