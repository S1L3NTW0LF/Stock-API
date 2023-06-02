import requests
import datetime

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

def extract_single_set_of_financial_statements(json_file, years_back=0):
    
    inc_data = json_file['income_data']['annualReports'][years_back]
    cas_data = json_file['cash_data']['annualReports'][years_back]
    bal_data = json_file['balance_data']['annualReports'][years_back]
                         
    return inc_data, cas_data, bal_data
                         
                         
def extract_stock_details(json_file):
    
    ticker = json_file['ticker']
    sector = json_file['sector']
    industry = json_file['industry']
    
    return ticker, sector, industry

def extract_price_data(json_file):
            
    price_data = json_file['price_data']
      
    return price_data

def changes_date_to_following_friday(weekday, first_date):
# changes the date to the following friday if it is a weekday 
    if  weekday == 1: # Monday  
        first_date += datetime.timedelta(11)
    elif weekday == 2: 
        first_date += datetime.timedelta(10)
    elif weekday == 3: 
        first_date += datetime.timedelta(9)
    elif weekday == 4: 
        first_date += datetime.timedelta(8)
    elif weekday == 5: 
        first_date += datetime.timedelta(7) 
    elif weekday == 6: 
        first_date += datetime.timedelta(6)
    elif weekday == 0: # Sunday 
        first_date += datetime.timedelta(5)

    return first_date
