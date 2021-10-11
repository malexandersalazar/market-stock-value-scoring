import yfinance as _yf

def get_usd_rate(currency):
    if (currency == 'USD'):
        return 1
    elif (currency == 'EUR'):
        return EUR_TO_USD
    elif (currency == 'GBp'):
        return GBP_TO_USD
    else:
        raise Exception("Unsupported currency!")

def _get_current_price(symbol):
    ticker = _yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]

EUR_TO_USD = 1 / _get_current_price('USDEUR=X')
GBP_TO_USD = 1 / _get_current_price('USDGBP=X')