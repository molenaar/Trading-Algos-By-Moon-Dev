# First Hour Brakout on QQQ trade Crypto 

overview
build a backtest that  looks at the QQQ in the first hour of the day and it makes a range from the high to the low of the first hour of the day, and makes the high and low. after the first hour of the day, it will keep those two prices in mind. if after the first hour, the price breaks out above the high, then we will say its a bullish day and if it breaks down below the first hours low, then we will call it a bearish day. 

after determining if its bearish or bullish, we will then trade bitcoin based off that indicator. so if its a bullish day, we would take a long on bitcoin and if it is bearish we would not trade, we would stay in cash. use backtesting.py for the backtest and polygon.io for the qqq data, and this for the crypto data: breakout_wick_algo/ETH-USD-15m-2018-1-02T00:00.csv

things to test
- what about shorting as well instead of staying in cash?

todo 
1. get data for crypto AND QQQ 
2. backtest it, improve back test to make sure it works and logic works