import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def analyze_stock_data(file_path):
    """Analyze stock trends and detect anomalies."""
    df = pd.read_csv(file_path, index_col=0, parse_dates=True)

    # Calculate Moving Averages
    df["SMA_20"] = df["Close"].rolling(window=20).mean()
    df["SMA_50"] = df["Close"].rolling(window=50).mean()

    # Detect Anomalies (Z-Score method)
    df["Price_Change"] = df["Close"].pct_change()
    df["Z-Score"] = (df["Price_Change"] - df["Price_Change"].mean()) / df["Price_Change"].std()
    df["Anomaly"] = df["Z-Score"].abs() > 3  # Mark anomalies

    # Plot Stock Prices with Moving Averages
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["Close"], label="Close Price", color="blue")
    plt.plot(df.index, df["SMA_20"], label="SMA 20", linestyle="dashed", color="green")
    plt.plot(df.index, df["SMA_50"], label="SMA 50", linestyle="dashed", color="red")
    plt.scatter(df.index[df["Anomaly"]], df["Close"][df["Anomaly"]], color="red", label="Anomaly", marker="o")
    plt.legend()
    plt.title("Stock Price Analysis with Moving Averages & Anomalies")
    plt.show()

    return df


if __name__ == "__main__":
    df_analyzed = analyze_stock_data("stock_data.csv")
    df_analyzed.to_csv("analyzed_stock_data.csv")
    print("Analysis completed. Saved as analyzed_stock_data.csv")
