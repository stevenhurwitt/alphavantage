from alpha_vantage.timeseries import TimeSeries as TimeSeriesOg
import multiprocessing
import datetime as dt
import pandas as pd
import numpy as np
import json
import os

with open('api_key.json', 'r') as f:
    api = json.load(f)
    api_key = api['api_key']

def get_ts(symbol):
    
    ts = TimeSeriesOg(key=api_key, output_format='pandas')
    data, meta_data = ts.get_daily_adjusted(symbol=symbol, outputsize='full')
    fname = "./data_dump/{}_data.csv".format(symbol)
    data.to_csv(fname)

def download_data(pool_id, symbols):
    for symbol in symbols:
        print("[{:02}]: {}".format(pool_id, symbol))
        get_ts(symbol)


if __name__ == "__main__":

    nasdaq = pd.read_csv('nasdaq_screener.csv')
    tickers = nasdaq.Symbol
    tickers = [a for a in tickers if '/' not in a]
    tickers = [a for a in tickers if '^' not in a]
    tickers = [a for a in tickers if 'AMP' not in a]

    # PROCESSES = multiprocessing.cpu_count()
    PROCESSES = 8  # number of parallel process
    CHUNKS = 6  # one process handle n symbols

    # create a list of n sublist
    tickers = [tickers[i:i + CHUNKS] for i in range(0, len(tickers), CHUNKS)]

    with multiprocessing.Pool(PROCESSES) as pool:
        pool.starmap(download_data, enumerate(tickers, start=1)) 
