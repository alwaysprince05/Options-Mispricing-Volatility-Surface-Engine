# Options Mispricing & Volatility Surface Engine

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Finance](https://img.shields.io/badge/Domain-Quantitative%20Finance-orange?style=for-the-badge)
![Model](https://img.shields.io/badge/Model-Black--Scholes-purple?style=for-the-badge)

**A modular, production-grade Python engine for detecting options mispricing, computing Greeks, and visualizing 3D volatility surfaces using the Black-Scholes model.**

*Built by [Prince Maurya](https://github.com/princemaurya)*

</div>

---

## Overview

This engine performs end-to-end quantitative analysis of options markets — from raw data ingestion to arbitrage opportunity detection and interactive visualization. It is designed to identify statistically significant price inefficiencies by comparing market prices against Black-Scholes theoretical values, then ranking them by Z-score deviation.

**Core use cases:**
- Detecting mispriced call/put options in a portfolio or market scan
- Visualizing the implied volatility smile and full 3D volatility surface
- Ranking arbitrage candidates by statistical significance
- Computing option Greeks for risk management

---

## Features

| Feature | Description |
|---|---|
| 📥 **Flexible Data Input** | Load options data via local CSV or live market data via `yfinance` |
| 📐 **Black-Scholes Pricing** | Manual implementation — no external pricing libraries, full transparency |
| 🧮 **Greeks Calculation** | Delta, Gamma, Vega, Theta — all computed analytically |
| 🎯 **Mispricing Detection** | Absolute & percentage mispricing with Z-score statistical ranking |
| 🌊 **Volatility Surface** | Interactive 3D surface plot (Plotly) + implied volatility smile (Matplotlib) |
| 🔥 **Mispricing Heatmap** | Strike vs. Expiry heatmap showing mispricing concentration |
| 📊 **Price Comparison** | Scatter plot of theoretical vs. market prices with regression line |
| 🏆 **Arbitrage Ranking** | Top 10 candidates sorted by absolute Z-score deviation |

---

## Project Architecture

```
Options-Mispricing-Volatility-Surface-Engine/
│
├── options_mispricing_engine/
│   ├── main.py           # CLI entry point & orchestration
│   ├── data_loader.py    # Data ingestion, cleaning & preprocessing
│   ├── pricing.py        # Black-Scholes pricing & mispricing logic
│   ├── greeks.py         # Option Greeks (Delta, Gamma, Vega, Theta)
│   ├── analysis.py       # Visualization & arbitrage ranking
│   ├── requirements.txt  # Python dependencies
│   └── sample.csv        # Example data for quick testing
│
├── README.md
└── LICENSE
```

---

## Modules

### `pricing.py` — Black-Scholes Engine
Implements the full Black-Scholes model from scratch using NumPy and SciPy:

$$C = S \cdot N(d_1) - K e^{-rT} \cdot N(d_2)$$
$$P = K e^{-rT} \cdot N(-d_2) - S \cdot N(-d_1)$$

where:
$$d_1 = \frac{\ln(S/K) + (r + \frac{\sigma^2}{2})T}{\sigma\sqrt{T}}, \quad d_2 = d_1 - \sigma\sqrt{T}$$

Also computes mispricing (absolute & percentage) and Z-scores across a dataset.

---

### `greeks.py` — Risk Sensitivities
Analytically computes all first-order Greeks:

| Greek | Formula |
|---|---|
| **Delta (Δ)** | $N(d_1)$ for call, $N(d_1) - 1$ for put |
| **Gamma (Γ)** | $\frac{N'(d_1)}{S\sigma\sqrt{T}}$ |
| **Vega (ν)** | $S \cdot N'(d_1) \cdot \sqrt{T}$ |
| **Theta (Θ)** | $-\frac{S N'(d_1)\sigma}{2\sqrt{T}} \mp rKe^{-rT}N(\pm d_2)$ |

---

### `analysis.py` — Visualization & Ranking
Generates five types of output:
- **Volatility Smile** — implied vol grouped by strike
- **3D Volatility Surface** — interactive Plotly surface (strike × time × IV)
- **Mispricing Heatmap** — strike vs. expiry color-coded by mispricing magnitude
- **Price Comparison Scatter** — market vs. theoretical with 45° reference line
- **Mispricing Histogram** — distribution of all pricing errors

---

### `data_loader.py` — Data Ingestion
Supports two modes:
- **CSV**: Reads structured options data from a local file
- **yfinance**: Fetches live options chain data for any ticker symbol

---

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/princemaurya/Options-Mispricing-Volatility-Surface-Engine.git
cd Options-Mispricing-Volatility-Surface-Engine

# Install dependencies
pip install -r options_mispricing_engine/requirements.txt
```

### Usage

**Run with a CSV file:**
```bash
python options_mispricing_engine/main.py --csv options_mispricing_engine/sample.csv --risk_free_rate 0.05
```

**Run with a live ticker (requires internet):**
```bash
python options_mispricing_engine/main.py --ticker AAPL --risk_free_rate 0.05
```

---

## CSV Input Format

Your CSV file must contain the following columns:

```
date,strike,expiry,option_type,market_price,underlying_price,implied_vol
```

| Column | Type | Description |
|---|---|---|
| `date` | date | Observation date |
| `strike` | float | Option strike price |
| `expiry` | date | Option expiration date |
| `option_type` | string | `call` or `put` |
| `market_price` | float | Observed market price |
| `underlying_price` | float | Current price of the underlying asset |
| `implied_vol` | float | Implied volatility (as decimal, e.g. `0.25` = 25%) |

---

## Output

The engine prints a summary to the terminal and opens interactive visualizations:

```
==== Metrics ====
mean_abs_mispricing: 0.42
max_deviation: 3.17
arbitrage_score: 7

==== Top 10 Arbitrage Candidates ====
   date  strike  expiry  option_type  market_price  theoretical_price  mispricing  zscore
...

==== Visualizations ====
[Opens 5 plots: smile, surface, heatmap, comparison, histogram]
```

---

## Dependencies

```
pandas
numpy
scipy
matplotlib
plotly
yfinance
```

Install all at once:
```bash
pip install -r options_mispricing_engine/requirements.txt
```

---

## License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

© 2026 Prince Maurya. All rights reserved.
