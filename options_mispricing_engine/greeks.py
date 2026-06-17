"""
greeks.py
Implements calculation of option Greeks for Black-Scholes model.
"""
import numpy as np
from scipy.stats import norm

class Greeks:
    def __init__(self, risk_free_rate=0.01):
        self.r = risk_free_rate

    def delta(self, S, K, T, sigma, option_type):
        d1 = (np.log(S/K) + (self.r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
        if option_type.lower() == 'call':
            return norm.cdf(d1)
        else:
            return norm.cdf(d1) - 1

    def gamma(self, S, K, T, sigma):
        d1 = (np.log(S/K) + (self.r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
        return norm.pdf(d1) / (S * sigma * np.sqrt(T))

    def vega(self, S, K, T, sigma):
        d1 = (np.log(S/K) + (self.r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
        return S * norm.pdf(d1) * np.sqrt(T)

    def theta(self, S, K, T, sigma, option_type):
        d1 = (np.log(S/K) + (self.r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
        d2 = d1 - sigma*np.sqrt(T)
        if option_type.lower() == 'call':
            return (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) - self.r * K * np.exp(-self.r * T) * norm.cdf(d2))
        else:
            return (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) + self.r * K * np.exp(-self.r * T) * norm.cdf(-d2))
