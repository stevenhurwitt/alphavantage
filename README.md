# alphavantage

Helping with a research project that involves downloading all the stock symbols in `nasdaq_screener.csv` using the alpha vantage API. 

The notebook shows how to download the data synchronously, while the `data_dump.py` file will download the data using multiprocessing (unless the API limit gets hit). `calc_years.py` calculates the years of data available for all stocks. This is then dumped into `year_calc_combined.csv` and appended to `nasdaq_years.csv`.