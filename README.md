
# Options Mispricing & Volatility Surface Engine

## Creator/Dev
## tubakhxn

## About This Project
This project is a modular Python engine for detecting option mispricing using the Black-Scholes model, visualizing volatility surfaces, and ranking arbitrage opportunities. It is designed for quantitative finance analysis and visualization.

## Features
- Data input via CSV or yfinance
- Black-Scholes pricing (manual implementation, no external pricing libraries)
- Greeks calculation (Delta, Gamma, Vega, Theta)
- Mispricing detection and statistical ranking
- Volatility smile and 3D volatility surface visualization
- Professional, object-oriented, modular structure

## How to Fork This Project
1. Click the **Fork** button on the top right of the GitHub repository page.
2. Clone your forked repository:
	```
	git clone https://github.com/yourusername/options-mispricing-vol-surface-engine.git
	```
3. Install requirements:
	```
	pip install -r options_mispricing_engine/requirements.txt
	```
4. Run the engine:
	```
	python options_mispricing_engine/main.py --csv path/to/data.csv --risk_free_rate 0.01
	```

## Files and Their Purpose
- **data_loader.py**: Data input, cleaning, and preprocessing
- **pricing.py**: Black-Scholes pricing and mispricing logic
- **greeks.py**: Greeks calculation (Delta, Gamma, Vega, Theta)
- **analysis.py**: Quantitative analysis, visualization, and ranking
- **main.py**: Orchestration, CLI, and end-to-end execution
- **requirements.txt**: Python dependencies
- **sample.csv**: Example data file for testing

## CSV Format
```
date,strike,expiry,option_type,market_price,underlying_price,implied_vol
```

## Requirements
- pandas
- numpy
- scipy
- matplotlib
- plotly
- yfinance

## License
MIT
