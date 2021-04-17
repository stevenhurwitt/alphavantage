from alpha_vantage.async_support.timeseries import TimeSeries
import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
import numpy as np
import asyncio
import os

api_key = "HXRGE747RBD2KVJ2"

async def get_data(symbol):
    ts = TimeSeries(key=api_key, output_format='pandas')
    
    try:
        data, _ = await ts.get_daily_adjusted(symbol=symbol, outputsize='full')
        await ts.close()
        fname = "./data_dump/{}_data.csv".format(symbol)
        data.to_csv(fname)

    except:
        pass
    return(None)

if __name__ == "__main__":

    nasdaq = pd.read_csv('nasdaq_screener.csv')
    loop = asyncio.get_event_loop()
    tasks = [get_data(symbol) for symbol in nasdaq.Symbol]
    group1 = asyncio.gather(*tasks)
    results = loop.run_until_complete(group1)
    print(results)