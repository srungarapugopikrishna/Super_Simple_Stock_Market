
from datetime import datetime
from datetime import timedelta
from src.models.Trade import Trade
from src.entities.Symbol import Symbol
from src.config_file import stocks_data


class Stock:
    def __init__(self, symbol: Symbol):
        """
        :param symbol: The symbol that identifies this stock
        """
        self.symbol = symbol
        for key, value in stocks_data[Symbol[symbol].value].items():
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
