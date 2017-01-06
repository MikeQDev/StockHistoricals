# StockHistoricals
Compare current stock prices to lowest historicals

This tool will assist in purchase predictions by allowing end-user to find all-time-low stock prices

(Written around Thanksgiving break 2016 to test out Python)

# Dependencies
Python

# How to use
1. Use symbolRetrieve.py to retreive a text-based list of stock tickers (given companylist.csv) **Write output to disk (python stockscrape.py [...] > tickers)
2. Use stockscrape.py to gather current and historical prices. **Write output to disk (python stockscrape.py [...] > prices)
3. Use analyzer.py to parse through stockscrape.py output - this will give ratio to base predictions on
