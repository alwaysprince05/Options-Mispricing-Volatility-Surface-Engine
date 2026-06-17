"""
data_loader.py
Handles data input, cleaning, and preprocessing for options mispricing engine.
"""
import pandas as pd
import yfinance as yf
from datetime import datetime

class DataLoader:
    def __init__(self, risk_free_rate=0.01):
        self.risk_free_rate = risk_free_rate

    def load_csv(self, file_path):
        df = pd.read_csv(file_path)
        return self._preprocess(df)

    def fetch_yfinance(self, ticker):
        # Placeholder: fetch option chain and underlying price
        # User must implement for their broker/data source
        raise NotImplementedError("Fetching option chain from yfinance is not fully supported.")

    def _preprocess(self, df):
        df = df.dropna()
        df['expiry'] = pd.to_datetime(df['expiry'])
        df['date'] = pd.to_datetime(df['date'])
        df['time_to_maturity'] = (df['expiry'] - df['date']).dt.days / 365.0
        return df

    def set_risk_free_rate(self, rate):
        self.risk_free_rate = rate
