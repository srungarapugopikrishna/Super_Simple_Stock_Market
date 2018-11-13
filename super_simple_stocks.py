
import enum
import operator
import random

from config_file import stocks
from datetime import datetime
from datetime import timedelta
from functools import reduce


@enum.unique
class Symbol(enum.Enum):

    TEA = 1
    POP = 2
    ALE = 3
    GIN = 4
    JOE = 5


class Trade:
    def __init__(self, timestamp: datetime, quantity, indicator, price):
        """
        :param timestamp: current timestamp
        :param quantity: quantity
        :param indicator: specifies this is a buy or sell
        :param price: price
        """
        self.timestamp = timestamp
        self.indicator = indicator
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Quantity should be greater than zero")
        if price > 0.0:
            self.price = price
        else:
            raise ValueError("Price should be greater than zero")

    def trade_cost(self):
        return self.quantity*self.price


class Stock:
    def __init__(self, symbol: Symbol):
        """
        :param symbol: The symbol that identifies this stock
        """
        self.symbol = symbol
        for key, value in stocks[Symbol[symbol].value].items():
            setattr(self, key, value)
        self.trades = []

    def dividend_yield(self, price) -> float:
        if self.stock_type == 'Common':
            return self.last_dividend/price
        else:
            return (self.fixed_dividend*self.par_value) / price

    def pe_ratio(self, price) -> float:
        if self.stock_type == 'Common':
            return price/self.last_dividend
        else:
            return price/self.fixed_dividend

    def record_trade(self, trade: Trade):
        self.trades.append(trade)

    def stock_price(self):
        current_time = datetime.now()
        recent_trades = [trade for trade in self.trades
                         if trade.timestamp >=
                         current_time - timedelta(minutes=5)]
        if len(recent_trades) > 0:
            for trade in recent_trades:
                trade_prices = [trade.trade_cost() for trade in recent_trades]
                quantities = (trade.quantity for trade in recent_trades)
                return sum(trade_prices) / sum(quantities)
        else:
            return None


class Utilities:

    @staticmethod
    def generate_random_timestamp():
        return (datetime.now() - timedelta(minutes=random.randint(1, 20),
                                           seconds=random.randint(1, 100),
                                           microseconds=random.randint(1,
                                                                       10000)))

    def create_trades(self):
        trades_list = []
        trade_details = []
        for i in range(50):
            time_stamp = self.generate_random_timestamp()
            quantity = random.randint(1, 50)
            indicator = random.randint(1, 2)
            price = random.randint(1, 150)
            trade_details.append([time_stamp, quantity, indicator, price])
            trade = Trade(time_stamp, quantity, indicator, price)
            trades_list.append(trade)
        return trades_list, trade_details

    @staticmethod
    def create_stock():
        stocks = ['TEA', 'POP', 'ALE', 'GIN', 'JOE']
        stocks_list = []
        for _ in range(5):
            stock_indx = random.randint(0, len(stocks) - 1)
            c_stock = Stock(stocks[stock_indx])
            stocks_list.append(c_stock)
            stocks.pop(stock_indx)
        return stocks_list

    @staticmethod
    def record_trades(stock_list, trades_list):
        for trade in trades_list:
            stock = stock_list[random.randint(0, len(stock_list)-1)]
            stock.record_trade(trade)


def all_price_index(stocks):
    n = len(stocks)
    stock_price_list = [stock.stock_price() for stock in stocks]
    if None in stock_price_list:
        return None
    else:
        product = reduce(operator.mul, stock_price_list, 1)
        return product ** (1 / n)
