"""
main.py
Entry point for Options Mispricing & Volatility Surface Engine.
"""
import argparse
import pandas as pd
from data_loader import DataLoader
from pricing import BlackScholes
from greeks import Greeks
from analysis import Analysis


def main():
    parser = argparse.ArgumentParser(description='Options Mispricing & Volatility Surface Engine')
    parser.add_argument('--csv', type=str, help='Path to CSV file')
    parser.add_argument('--ticker', type=str, help='Ticker symbol')
    parser.add_argument('--risk_free_rate', type=float, default=0.01, help='Risk-free rate')
    args = parser.parse_args()

    loader = DataLoader(risk_free_rate=args.risk_free_rate)
    if args.csv:
        df = loader.load_csv(args.csv)
    elif args.ticker:
        df = loader.fetch_yfinance(args.ticker)
    else:
        print('Please provide either --csv or --ticker')
        return

    bs = BlackScholes(risk_free_rate=args.risk_free_rate)
    greeks = Greeks(risk_free_rate=args.risk_free_rate)
    analysis = Analysis(risk_free_rate=args.risk_free_rate)

    theoretical_prices = []
    mispricings = []
    pct_mispricings = []
    greeks_delta = []
    greeks_gamma = []
    greeks_vega = []
    greeks_theta = []

    for idx, row in df.iterrows():
        S = row['underlying_price']
        K = row['strike']
        T = row['time_to_maturity']
        sigma = row['implied_vol']
        option_type = row['option_type']
        market_price = row['market_price']

        if option_type.lower() == 'call':
            theo = bs.call_price(S, K, T, sigma)
        else:
            theo = bs.put_price(S, K, T, sigma)
        theoretical_prices.append(theo)

        diff, pct = bs.mispricing(market_price, theo)
        mispricings.append(diff)
        pct_mispricings.append(pct)

        greeks_delta.append(greeks.delta(S, K, T, sigma, option_type))
        greeks_gamma.append(greeks.gamma(S, K, T, sigma))
        greeks_vega.append(greeks.vega(S, K, T, sigma))
        greeks_theta.append(greeks.theta(S, K, T, sigma, option_type))

    df['theoretical_price'] = theoretical_prices
    df['mispricing'] = mispricings
    df['pct_mispricing'] = pct_mispricings
    df['delta'] = greeks_delta
    df['gamma'] = greeks_gamma
    df['vega'] = greeks_vega
    df['theta'] = greeks_theta
    df['zscore'] = bs.zscore(mispricings)

    metrics = analysis.compute_metrics(df)
    top_arbitrage = analysis.rank_arbitrage(df)

    print("\n==== Metrics ====")
    for k, v in metrics.items():
        print(f"{k}: {v}")
    print("\n==== Top 10 Arbitrage Candidates ====")
    print(top_arbitrage[['date','strike','expiry','option_type','market_price','theoretical_price','mispricing','zscore']])

    print("\n==== Visualizations ====")
    analysis.implied_vol_smile(df)
    analysis.volatility_surface(df)
    analysis.mispricing_heatmap(df)
    analysis.price_comparison(df)
    analysis.mispricing_histogram(df)

if __name__ == '__main__':
    main()
