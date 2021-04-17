# alphavantage

Helping with a research project that involves downloading all the stock symbols in `nasdaq_screener.csv` using the alpha vantage API. 

The notebook shows how to download the data synchronously, while the `data_dump.py` file will download the data using multiprocessing (unless the API limit gets hit).