"""
pricing.py
Implements Black-Scholes pricing and mispricing detection.
"""
import numpy as np
from scipy.stats import norm

class BlackScholes:
    def __init__(self, risk_free_rate=0.01):
        self.r = risk_free_rate

    def d1(self, S, K, T, sigma):
        return (np.log(S/K) + (self.r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))

    def d2(self, S, K, T, sigma):
        return self.d1(S, K, T, sigma) - sigma*np.sqrt(T)

    def call_price(self, S, K, T, sigma):
        d1 = self.d1(S, K, T, sigma)
        d2 = self.d2(S, K, T, sigma)
        return S*norm.cdf(d1) - K*np.exp(-self.r*T)*norm.cdf(d2)

    def put_price(self, S, K, T, sigma):
        d1 = self.d1(S, K, T, sigma)
        d2 = self.d2(S, K, T, sigma)
        return K*np.exp(-self.r*T)*norm.cdf(-d2) - S*norm.cdf(-d1)

    def mispricing(self, market_price, theoretical_price):
        diff = market_price - theoretical_price
        pct = diff / theoretical_price * 100 if theoretical_price != 0 else np.nan
        return diff, pct

    def zscore(self, mispricings):
        mean = np.mean(mispricings)
        std = np.std(mispricings)
        return [(x - mean)/std if std != 0 else np.nan for x in mispricings]
