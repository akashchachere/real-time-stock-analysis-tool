import time
import os
from fetch_stock_data import get_stock_data
from analyze_stock import analyze_stock_data

STOCK_SYMBOL = "AAPL"  # Change as needed
UPDATE_INTERVAL = 300  # Update every 5 minutes (300 seconds)

while True:
    print(f"Fetching data for {STOCK_SYMBOL}...")
    df = get_stock_data(STOCK_SYMBOL)

    if df is not None:
        df.to_csv("stock_data.csv")
        print("Stock data updated.")

        print("Performing analysis...")
        analyze_stock_data("stock_data.csv")
        print("Analysis updated.")

    print(f"Next update in {UPDATE_INTERVAL / 60} minutes...")
    time.sleep(UPDATE_INTERVAL)
