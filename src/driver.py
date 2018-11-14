
from src.Utilities import Utilities
from src.Utilities import all_price_index

utility = Utilities()
stock_list = utility.create_stock()
print(stock_list)
trade_list, trade_details = utility.create_trades()
print(trade_details)
# recoding trades
utility.record_trades(stock_list, trade_list)

stock_price_list = {stock.symbol: stock.stock_price() for stock in stock_list}

print('Volume Weighted Stock Price based on trades in past 5 minutes:')
print(stock_price_list)
gbce_share_indx = all_price_index(stock_list)
print('\nGBCE All Share Index :', gbce_share_indx)
if gbce_share_indx is None:
    print('\n\nNote: If there are no trades for any stock in the past '
          '5 minutes then GBCE all share index will be none because '
          'Volume Weighted  Stock Price is calculated based on trades in '
          'past 5 minutes')
