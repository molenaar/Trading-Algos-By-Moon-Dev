# Breakout Wick Algo

overview:
this algo will wait for a breakout on the 5 min. the next 3 bars, it will watch where those wicks are on the downside. the wick will be between the close and the low. then on the 4-10 bar, it will try to buy those wick areas that were in the first 3 bars. use a take profit of 3% and stop loss of 3%. use the optimizer to test the different number of bars to watc wicks for to see which work best and also use the optimzer in ordeer to test the different stop losses and take profits. use this data for the backtest: breakout_wick_algo/ETH-USD-15m-2018-1-02T00:00.csv

see the example.png to see what im talking about. 

resources: 


Todo 
0. grab data from datasource, test diff time periods
1. tweak the backtest to make sure it works properly
2. test different variables like: timeframe, how many bars to watch for wicks, symbols (a lot of this can be done with the optimizer)