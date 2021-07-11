#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from scipy import stats
from statistics import mean
from datetime import datetime as DateTime
import yfinance as yf
import pytickersymbols as pts

# ## Acquiring information about stocks 

# In[4]:


stock_data = pts.PyTickerSymbols()

eu50_stocks = stock_data.get_stocks_by_index('EURO STOXX 50')
us30_stocks = stock_data.get_stocks_by_index('DOW JONES')
uk100_stocks = stock_data.get_stocks_by_index('FTSE 100')
us100_stocks = stock_data.get_stocks_by_index('S&P 100')

market_stocks = list(eu50_stocks) + list(us30_stocks) + list(uk100_stocks) + list(us100_stocks)

excluded_sectors = ['Biotechnology & Medical Research','Online gambling','Pharmaceuticals','Healthcare','Managed Health care','Medical Equipment','Banking & Investment Services','Medical Equipment, Supplies & Distribution','Metals & Mining','Metal','Insurance','Commercial REITs','Specialized REITs','Financial services','Beverages','Food & Beverages','Real Estate','Casinos & Gaming','Fossil Fuels']

stocks_list = []
for market_stock in market_stocks:
    try:
        ignore = False
        for market_industry in market_stock['industries']:
            if(market_industry in excluded_sectors):
                ignore = True
                break
            
        if(ignore):
            continue

        stock_symbol = market_stock['symbol']
        symbols = market_stock['symbols']

        symbol_google = None
        symbol_yahoo = None
        for symbol in symbols:
            if(symbol['google'].endswith(f':{stock_symbol}')):
                symbol_google = symbol['google']
                symbol_yahoo = symbol['yahoo']
                break

        if(symbol_yahoo is None):
            continue

        item = {
            'Company': market_stock['name'],
            'Symbol': stock_symbol,
            'Symbol_Google': symbol_google,
            'Symbol_Yahoo': symbol_yahoo,
            'Country': market_stock['country'],
            'Indices': ', '.join(market_stock['indices']),
            'Sectors': ', '.join(market_stock['industries'])
        }

        stocks_list.append(item)
    except:
        pass

stocks = pd.DataFrame(stocks_list, columns=['Company','Symbol','Symbol_Google','Symbol_Yahoo','Country','Indices','Sectors'])

# In[5]:


# Some stocks are listed on more than the stock index.
stocks.set_index('Symbol',inplace=True)
stocks = stocks[~stocks.index.duplicated(keep='first')]

# ## Transforming data for value calculation 

# In[6]:


# Defining stocks value scoring dataframe

df_columns = [
    'Company',
    'Symbol',
    'Symbol_Google',
    'Symbol_Yahoo',
    'Description',
    'Country',        
    'Indices',
    'Sectors',
    'MarketCap',
    'Price',
    'Currency',
    'PriceToEarningsRatio',
    'PriceToEarningsPercentile',
    'PriceToSalesRatio',
    'PriceToSalesPercentile',
    'EV_EBITDA',
    'EV_EBITDAPercentile',
    'EV_R',
    'EV_RPercentile',
    'Score'
]

so_dataframe = pd.DataFrame(columns = df_columns)

# Getting fundamental data
i = 0
total_stocks = len(stocks)
errors = 0
for index, stock in stocks.iterrows():
    i+=1
    stock_name = stock['Company']
    symbol = index

    symbol_google = stock['Symbol_Google']
    symbol_yahoo = stock['Symbol_Yahoo']

    print(f'({i}/{total_stocks}) | {symbol} (Google: {symbol_google}, Yahoo: {symbol_yahoo}) | {stock_name}')
    print(f'Retreiving fundamental data from yfinance...')

    try:
        yf_ticker = yf.Ticker(symbol_yahoo)
        so_dataframe = so_dataframe.append(
            pd.Series([
                stock_name,
                symbol,
                symbol_google,
                symbol_yahoo,
                yf_ticker.info['longBusinessSummary'],
                stock['Country'],
                stock['Indices'],
                stock['Sectors'],
                yf_ticker.info['marketCap'],
                yf_ticker.info['regularMarketPrice'],
                yf_ticker.info['currency'],
                yf_ticker.info['trailingPE'],
                'N/A',
                yf_ticker.info['priceToSalesTrailing12Months'],
                'N/A',
                yf_ticker.info['enterpriseToEbitda'],
                'N/A',
                yf_ticker.info['enterpriseToRevenue'],
                'N/A',
                'N/A'
            ], index = df_columns),
            ignore_index = True)

    except Exception as error:
        print('ERROR:', error)
        errors+=1
        print('An error occurred while trying to get the information!')
        
    print()

initial_count = len(so_dataframe)

# Dealing With Missing Data
so_dataframe = so_dataframe.dropna()


# In[7]:


# Calculating percentiles
print('Calculating Percentiles...')

metrics = {
    'PriceToEarningsRatio': 'PriceToEarningsPercentile',
    'PriceToSalesRatio': 'PriceToSalesPercentile',
    'EV_EBITDA':'EV_EBITDAPercentile',
    'EV_R':'EV_RPercentile'
}

for row in so_dataframe.index:
    for metric in metrics.keys():
        if(metric == 'PriceToSalesRatio' or metric == 'EV_R'):
            so_dataframe.loc[row, metrics[metric]] = stats.percentileofscore(1 / so_dataframe[metric], 1 / so_dataframe.loc[row, metric])
        else:
            so_dataframe.loc[row, metrics[metric]] = stats.percentileofscore(so_dataframe[metric], so_dataframe.loc[row, metric])

# Scoring stocks
print('Scoring Stocks...')
for row in so_dataframe.index:
    value_percentiles = []
    for metric in metrics.keys():
        value_percentiles.append(so_dataframe.loc[row, metrics[metric]])
    so_dataframe.loc[row, 'Score'] = mean(value_percentiles)

# Sorting and selecting
result_df = so_dataframe[so_dataframe['Score'] > 50].copy()
result_df.sort_values(by = 'Score', inplace = True, ascending=False)

skipped_count = initial_count - len(result_df)
now = DateTime.now()

print()
print(f'Scoring executed successfully at {now.hour}:{now.minute} | {total_stocks} listed | {errors} not found | {skipped_count} incomplete | {len(result_df)} selected')

# In[10]:


writer = pd.ExcelWriter('market_stock_value_scoring.xlsx', engine='xlsxwriter')
result_df.to_excel(writer, sheet_name='Value Scoring', index = False)

# Defining Excel columns formats and templates
background_light_color = '#ffffff'
background_dark_color = '#eeeeee'
background_accent_color = '#0086CD'
black_color = '#000000'
white_color = '#ffffff'

string_template = writer.book.add_format(
        {
            'font_color': black_color,
            'bg_color': background_light_color,
            'border': 0
        }
    )

float_template = writer.book.add_format(
        {
            'num_format':'0.000',
            'font_color': black_color,
            'bg_color': background_light_color,
            'border': 0
        }
    )

percentile_template = writer.book.add_format(
        {
            'num_format':'0.000',
            'font_color': black_color,
            'bg_color': background_dark_color,
            'border': 0
        }
    )

score_template = writer.book.add_format(
        {
            'num_format':'0.000',
            'font_color': white_color,
            'bg_color': background_accent_color,
            'border': 0
        }
    )

print('Saving in Excel...\n')

column_formats = {
    'A': ['Stock', string_template],
    'B': ['Symbol', string_template],
    'C': ['Symbol_Google', string_template],
    'D': ['Symbol_Yahoo', string_template],
    'E': ['Description', string_template],
    'F': ['Country', string_template],
    'G': ['Indices', string_template],
    'H': ['Sectors', string_template],
    'I': ['MarketCap', float_template],
    'J': ['Price', float_template],
    'K': ['Currency', string_template],
    'L': ['PriceToEarningsRatio', float_template],
    'M': ['PriceToEarningsPercentile', percentile_template],
    'N': ['PriceToSalesRatio', float_template],
    'O': ['PriceToSalesPercentile', percentile_template],
    'P': ['EV_EBITDA', float_template],
    'Q': ['EV_EBITDAPercentile', percentile_template],
    'R': ['EV_R', float_template],
    'S': ['EV_RPercentile', percentile_template],
    'T': ['Score', score_template]
}

for column in column_formats.keys():
    writer.sheets['Value Scoring'].set_column(f'{column}:{column}', 25, column_formats[column][1])
    writer.sheets['Value Scoring'].write(f'{column}1', column_formats[column][0], column_formats[column][1])

writer.save()

