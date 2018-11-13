
from datetime import datetime


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
