from pandas.util.testing import assert_frame_equal
import pandas_datareader as data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import cufflinks as cf
import numpy as np
import datetime

cf.go_offline()
sns.set_style('whitegrid')
start = datetime.datetime(2006, 1, 1)         #(year,month,date)
end = datetime.datetime(2016, 1, 1)
BAC = data.DataReader('BAC', 'yahoo', start, end)
C = data.DataReader('C', 'yahoo', start, end)
GS = data.DataReader('GS', 'yahoo', start, end)
JPM = data.DataReader('JPM', 'yahoo', start, end)
MS = data.DataReader('MS', 'yahoo', start, end)
WFC = data.DataReader('WFC', 'yahoo', start, end)

tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']
bank_stocks = pd.concat([BAC, C, GS, JPM, MS, WFC], axis=1, keys=tickers)
bank_stocks.columns.names = ['Bank Ticker', 'Stock Info']

#for tick in tickers:
#    print(tick, '\t', bank_stocks[tick]['Close'].max())

returns = pd.DataFrame()
for tick in tickers:
    returns[tick + ' Returns'] = bank_stocks[tick]['Close'].pct_change()
#print(returns)

#sns.pairplot(returns[1:])
#plt.show()

#print('Dates for minimum returns :')
#print(returns.idxmin())
#print()
#print('Dates for maximum returns :')
#print(returns.idxmax())

#print('Standard deviation for all companies throughout the mentioned time period :')
#print(returns.std())
#print()
#print('Standard deviation for all companies in the year 2015 :')
#print(returns.loc['2015-01-01': '2015-12-31'].std())     # Slicing up of data in the dataframe

#sns.distplot(returns.loc['2015-01-01':'2015-12-31']['MS Returns'], bins=50)
#sns.distplot(returns.loc['2008-01-01':'2008-12-31']['C Returns'], color='green', bins=50)

#for tick in tickers:
#    bank_stocks[tick]['Close'].iplot(figsize=(12,4))

#plt.figure(figsize=(12,4))
#BAC['Close'].loc['2008-01-01':'2008-12-31'].rolling(window=30).mean().plot(label='30 Day Mov Avg')
#BAC['Close'].loc['2008-01-01':'2008-12-31'].plot(label='BAC Close')
#plt.legend()

#sns.heatmap(bank_stocks.xs(key='Close', axis=1, level='Stock Info').corr(), annot=True)

close_corr = bank_stocks.xs(key='Close', axis=1, level='Stock Info').corr()
close_corr.iplot(kind='heatmap', colorscale='rdylbu')
plt.show()