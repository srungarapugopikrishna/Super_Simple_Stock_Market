                                Super Simple Stock Market

Execute driver.py

Data is populated dynamically from utility functions create_trades() and 
create_stock().
Values differ for every run(Because it is based on current timestamp).

Static constraints:
I am creating a whole of 50 trades and assigning them to stocks.

While calculating Volume Weighted Stock Price based on trades in past  5 minutes, if there are no trades happened for this stock in the past 5 minutes I am assuming that this will be None .

As a result if it is None, GBCE All Share Index will be None.
