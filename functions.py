import requests

def make_api_call_for_financial_statements(symbol, key):
    
    # if symbol is not valid then it will return an empty json object
    income_api_url = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey={key}'
    income_data = requests.get(income_api_url).json()

    cash_api_url = f'https://www.alphavantage.co/query?function=CASH_FLOW&symbol={symbol}&apikey={key}'
    cash_data = requests.get(cash_api_url).json()

    balance_api_url = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={symbol}&apikey={key}'
    balance_data = requests.get(balance_api_url).json()
    
    return income_data, cash_data, balance_data

def make_api_call_for_price_time_series(symbol, key):
    
    # if symbol is not valid then it will return an empty json object
    price_api_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={symbol}&outputsize=full&apikey={key}'
    price_data = requests.get(price_api_url).json()
    
    return price_data

def extract_single_set_of_financial_statements(income_data, cashflow_data, balancesheet_data, years_back):
    
    years_back += 1
    
    inc_data = income_data['annualReports'][-years_back].copy()
    cas_data = cashflow_data['annualReports'][-years_back].copy()
    bal_data = balancesheet_data['annualReports'][-years_back].copy()
    
    return inc_data, cas_data, bal_data

