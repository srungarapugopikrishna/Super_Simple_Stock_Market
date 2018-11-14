import unittest

from src.models.Stock import Stock


class TestStockMethods(unittest.TestCase):
    def test_dividend_yield(self):
        stock = Stock('POP')
        self.assertEqual(stock.dividend_yield(135.0), 0.05925925925925926)

    def test_pe_ratio(self):
        stock = Stock('JOE')
        self.assertTrue(stock.pe_ratio(98.0), 7.538461538461538)


if __name__ == '__main__':
    unittest.main()
