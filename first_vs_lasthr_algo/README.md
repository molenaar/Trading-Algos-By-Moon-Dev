# First Hour vs Last Hour Trading Algo

overview: 
build me a backtest with backtesting.py that watches what happens in the morning session of the QQQ and then assumes that the closing will be similar action to the first hour of the US qqq session. so if the first hour of the QQQ US session was upwards, we will assume the closing session will be the same. please build a backtest for that

also build a backtest for the opposite, so if the morning sessions (first hour) is up, then we would assume the afternoon session (last hour) is going to be down. 

output both of these backtests 

resources: https://www.luxeeai.com//backtesting-qqq-morning-session-closing-session-strategy-python 

Tests
- test with crypto. if qqq is up in first hour, does that mean last hour of crypto up? or opposite?

TODO 
1. get data from polygon on the QQQ / ES1 / APPL
2. see if it mimicks the first hour, or does opposite
3. test with crypto too
    test 1- hows it react based on the stock data
    test 2- how about btc data, first hour on btc vs closing hour 3-4pm est. 