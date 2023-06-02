# Stock API
##### Retrieves json objects from API then converts them into csv files for later analysis

---
### Part I (collect_data.ipynb)
- loops through all ticker symbols found on the brokerage Fidelity's website as of 2022
- makes api calls for income statement, balance sheet, cashflow statement, and weekly price data
- data is placed into a dictionary and then written into json_files folder

### Part II (stock-json.ipynb)
- loops through all files in json_files folder
- transforms json file into dataframes 
- calculates the yearly percent price change following earnings announcement
- writes individual stock data into stock-sets folder
- writes all data to master-df.csv

---
### Notes
- stock data only goes back up to 5 years
- percent price change is calcuated using weekly prices from 5-11 days after to 341-347 after
- functions.py contains functions used in notebooks
- different errors are written to csv files in errors-list folder
- screener_results.csv contain all the stocks found on Fidelity website
- The API being used is from AlphaVantage (https://www.alphavantage.co/)
- other notebooks are similar previous versions 
