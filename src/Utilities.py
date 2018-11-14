
from datetime import datetime
from datetime import timedelta
from src.models.Stock import Stock
from src.models.Trade import Trade
from functools import reduce
import operator

import random


class Utilities:
    def __init__(self):
        pass

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
            print(stock_indx)
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
