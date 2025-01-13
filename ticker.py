# ticker.py
import datetime
import requests_cache
import matplotlib.pyplot as plt
from pandas_datareader import data as wb

class Ticker:
    """Class for fetching data from yahoo finance."""
    
    @staticmethod
    def get_historical_data(ticker, start_date=None, end_date=None, cache_days=1):
        """
        Fetches stock data from yahoo finance. Request is by default cached in sqlite db for 1 day.
        
        Params:
        ticker: ticker symbol
        start_date: start date for getting historical data
        end_date: end date for getting historical data
        cache_days: number of days data will stay in cache 
        """
        try:
            # initializing sqlite for caching yahoo finance requests
            expire_after = datetime.timedelta(days=cache_days)
            session = requests_cache.CachedSession(cache_name='cache', backend='sqlite', expire_after=expire_after)

            # Adding headers to session
            session.headers = {'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json;charset=utf-8'}
            
            if start_date is not None and end_date is not None:
                data = wb.DataReader(ticker, data_source='yahoo', start=start_date, end=end_date, session=session)
            else:
                data = wb.DataReader(ticker, data_source='yahoo', session=session)
            if data is None:
                return None
            return data
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def get_columns(data):
        """Gets dataframe columns from previously fetched stock data."""
        if data is None:
            return None
        return [column for column in data.columns]

    @staticmethod
    def get_last_price(data, column_name):
        """Returns last available price for specified column from already fetched data."""
        if data is None or column_name is None:
            return None
        if column_name not in Ticker.get_columns(data):
            return None
        return data[column_name].iloc[-1]

    @staticmethod
    def plot_data(data, ticker, column_name):
        """Plots specified column values from dataframe."""
        try:
            if data is None:
                return
            data[column_name].plot()
            plt.ylabel(f'{column_name}')
            plt.xlabel('Date')
            plt.title(f'Historical data for {ticker} - {column_name}')
            plt.legend(loc='best')
            plt.show()
        except Exception as e:
            print(e)
            return
