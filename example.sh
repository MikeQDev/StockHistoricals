#!/bin/bash

#grab first field (ticker) of each row in csv file
python 1-symbolRetrieve.py data/companylist.csv > tickers
#scrape google to find current prices, scrape yahoo to find historicals; outputs base-data.csv
python 2-stockscrape.py tickers
#use the scraped base-data (cur and historical price) to find ratio, etc.
python 3-analyzer.py base-data.csv > analyzed
#output to graph
python 4-graph-scraper.py analyzed
