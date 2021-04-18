from alpha_vantage.timeseries import TimeSeries as TimeSeries
import multiprocessing
import datetime as dt
import pandas as pd
import numpy as np
import json
import os

def get_years(symbol):
    fname = "./data_dump/{}_data.csv".format(symbol)
    data = pd.read_csv(fname)
    data.date = pd.to_datetime(data.date)
    last_date = np.max(data.date)
    first_date = np.min(data.date)
    years = round((last_date - first_date).days / 365,2)
    return(years)

def year_calc(pool_id, symbols):
    years_list = []
    symbols_list = []

    for symbol in symbols:
        print("[{:02}]: {}".format(pool_id, symbol))

        try:
            years = get_years(symbol)
            years_list.append(years)
            symbols_list.append(symbol)

        except:
            pass

    print('writing data to .csv...')
    output = dict(zip(symbols_list, years_list))
    output_df = pd.DataFrame.from_dict(output, orient = 'index')
    fname = './year_calc/year_calc_{}.csv'.format(pool_id)
    output_df.to_csv(fname, header = False)
    print('done.')


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
        pool.starmap(year_calc, enumerate(tickers, start=1)) 