import pandas as pd
from scipy import stats
from statistics import mean
from datetime import datetime as DateTime
import yfinance as yf
import pytickersymbols as pts
import stocks_utils as sou

def run():
    stock_data = pts.PyTickerSymbols()

    us30_stocks = stock_data.get_stocks_by_index('DOW JONES')
    nasdaq_stocks = stock_data.get_stocks_by_index('NASDAQ 100')
    us500_stocks = stock_data.get_stocks_by_index('S&P 500')
    uk100_stocks = stock_data.get_stocks_by_index('FTSE 100')
    eu50_stocks = stock_data.get_stocks_by_index('EURO STOXX 50')

    market_stocks = list(us30_stocks) + list(nasdaq_stocks) + list(us500_stocks) + list(uk100_stocks) + list(eu50_stocks)

    excluded_industries = ['Online gambling','Healthcare','Managed Health care','Banking & Investment Services','Metals & Mining','Metal','Insurance','Commercial REITs','Specialized REITs','Financial services','Real Estate','Casinos & Gaming','Fossil Fuels','Defense','Cosmetics','defense','Life insurance','Real estate investment trust']

    stocks_list = []
    for market_stock in market_stocks:
        try:
            ignore = False
            for market_industry in market_stock['industries']:
                if(market_industry in excluded_industries):
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
                'Industries': ', '.join(market_stock['industries'])
            }

            stocks_list.append(item)
        except:
            pass

    stocks = pd.DataFrame(stocks_list, columns=['Company','Symbol','Symbol_Google','Symbol_Yahoo','Country','Indices','Industries'])
    stocks.set_index('Symbol',inplace=True)
    stocks = stocks[~stocks.index.duplicated(keep='first')]

    df_columns = [
        'Company',
        'Symbol',
        'Symbol_Google',
        'Symbol_Yahoo',
        'Description',
        'Country',        
        'Indices',
        'Industries',
        'MarketCap',
        'Y1HighestPriceValue',
        'Y1HighestPriceDate',
        'Currency',
        'PriceToEarningsRatio',
        'PriceToEarningsPercentile',
        'PriceToEarningsInversePercentile',
        'PriceToSalesRatio',
        'PriceToSalesPercentile',
        'PriceToSalesInversePercentile',
        'EV_EBITDA',
        'EV_EBITDAPercentile',
        'EV_R',
        'EV_RPercentile',
        'EV_RInversePercentile',
        'Score_Long',
        'Score_Short'
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

            day_data = yf_ticker.history(period="1y", interval="1d")
            day_data.dropna(inplace=True)
            day_data.sort_values('High', ascending=False, inplace=True)

            so_dataframe = so_dataframe.append(
                pd.Series([
                    stock_name,
                    symbol,
                    symbol_google,
                    symbol_yahoo,
                    yf_ticker.info['longBusinessSummary'],
                    stock['Country'],
                    stock['Indices'],
                    stock['Industries'],
                    yf_ticker.info['marketCap'],
                    day_data.iloc[0]['High'],
                    day_data.index[0].strftime('%Y-%m-%d'),
                    yf_ticker.info['currency'],
                    yf_ticker.info['trailingPE'],
                    'N/A',
                    'N/A',
                    yf_ticker.info['priceToSalesTrailing12Months'],
                    'N/A',
                    'N/A',
                    yf_ticker.info['enterpriseToEbitda'],
                    'N/A',
                    yf_ticker.info['enterpriseToRevenue'],
                    'N/A',
                    'N/A',
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
    so_dataframe = so_dataframe[so_dataframe['Industries']!=''].dropna()


    # Calculating percentiles
    print('Calculating percentiles...')

    metrics_long = {
        'PriceToEarningsRatio': 'PriceToEarningsPercentile',
        'PriceToSalesRatio': 'PriceToSalesInversePercentile',
        'EV_EBITDA':'EV_EBITDAPercentile',
        'EV_R':'EV_RInversePercentile'
    }

    metrics_short = {
        'PriceToEarningsRatio': 'PriceToEarningsInversePercentile',
        'PriceToSalesRatio': 'PriceToSalesPercentile',
        'EV_R':'EV_RPercentile'
    }

    for row in so_dataframe.index:
        for metric in metrics_long.keys():
            if(metric == 'PriceToSalesRatio' or metric == 'EV_R'):
                so_dataframe.loc[row, metrics_long[metric]] = stats.percentileofscore(1 / so_dataframe[metric], 1 / so_dataframe.loc[row, metric])
            else:
                so_dataframe.loc[row, metrics_long[metric]] = stats.percentileofscore(so_dataframe[metric], so_dataframe.loc[row, metric])

        for metric in metrics_short.keys():
            if(metric == 'PriceToEarningsRatio'):
                so_dataframe.loc[row, metrics_short[metric]] = stats.percentileofscore(1 / so_dataframe[metric], 1 / so_dataframe.loc[row, metric])
            else:
                so_dataframe.loc[row, metrics_short[metric]] = stats.percentileofscore(so_dataframe[metric], so_dataframe.loc[row, metric])
                

    # Scoring stocks
    print('Scoring stocks...')
    for row in so_dataframe.index:
        value_percentiles = []
        for metric in metrics_long.keys():
            value_percentiles.append(so_dataframe.loc[row, metrics_long[metric]])
        so_dataframe.loc[row, 'Score_Long'] = mean(value_percentiles)

        value_percentiles = []
        for metric in metrics_short.keys():
            value_percentiles.append(so_dataframe.loc[row, metrics_short[metric]])
        so_dataframe.loc[row, 'Score_Short'] = mean(value_percentiles)

    # Sorting and selecting
    result_df = so_dataframe.copy()
    result_df.sort_values(by = 'Company', inplace = True, ascending=True)
    result_df['MarketCap_USD'] = result_df['MarketCap'] * result_df['Currency'].apply(sou.get_usd_rate)
    result_df = result_df[['Company','Symbol','Symbol_Google','Symbol_Yahoo','Description','Country','Indices','Industries','Currency','MarketCap','MarketCap_USD','Y1HighestPriceValue','Y1HighestPriceDate', 'PriceToEarningsRatio','PriceToEarningsPercentile','PriceToEarningsInversePercentile','PriceToSalesRatio','PriceToSalesPercentile','PriceToSalesInversePercentile','EV_EBITDA','EV_EBITDAPercentile','EV_R','EV_RPercentile','EV_RInversePercentile','Score_Long','Score_Short']]
    skipped_count = initial_count - len(result_df)
    now = DateTime.now()

    print()
    print(f'Scoring executed successfully at {now.hour}:{now.minute} | {total_stocks} listed | {errors} not found | {skipped_count} skipped | {len(result_df)} scored stocks')

    return result_df