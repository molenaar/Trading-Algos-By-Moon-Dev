# Liquidation Bot

strategy overview - 
trading strategy using backtesting.py that buys after there is a huge volume spike (10x the average) and price is moving downward

then wait to buy til the price moves back down to near where the volume spike was, whatever that price was

so essentially we are marking the price of when the 10x volume spike happened, and then we are waiting til the next bar and we enter long when the next bar gets near that volume spike price. 

* see the trade_example.png for a good example of when we would enter this trade. waiting for a big volume spike and then waiting for the second drawdown near that area to enter. 

resources
- https://www.luxeeai.com//mastering-python-trading-strategies-backtesting-guide 