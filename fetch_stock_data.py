import requests
import pandas as pd
import time

# Alpha Vantage API Key (Get yours from https://www.alphavantage.co/)
API_KEY = "HAW5AUB5JYGE8HE8"
BASE_URL = "https://www.alphavantage.co/query"


def get_stock_data(symbol):
    """Fetch real-time stock data from Alpha Vantage."""
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": "5min",
        "apikey": API_KEY,
        "datatype": "json"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if "Time Series (5min)" not in data:
        print("Error fetching data:", data)
        return None

    df = pd.DataFrame.from_dict(data["Time Series (5min)"], orient="index")
    df.columns = ["Open", "High", "Low", "Close", "Volume"]
    df.index = pd.to_datetime(df.index)
    df = df.astype(float)  # Convert data types
    df = df.sort_index()  # Ensure correct time ordering

    return df


if __name__ == "__main__":
    stock_symbol = "AAPL"  # Change stock symbol as needed
    df = get_stock_data(stock_symbol)
    if df is not None:
        df.to_csv("stock_data.csv")
        print("Data saved to stock_data.csv")
