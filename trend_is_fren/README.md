# trend is your fren

build me a backtest that shows buying bitcoin in 6 hours waves... so it will be long for 6 hours after a consolitation and then close after a move upward, wait for another 6 hour consolidation and then enter and wait for another move.. show me all the backtesting code

https://www.luxeeai.com//mastering-bitcoin-waves-backtest-strategy-6-hour-trading-waves

analyzing the trend file: https://www.luxeeai.com//analyzing-price-trends-longevity-upward-downward-sideways-movements 

backtest: https://www.luxeeai.com//python-backtest-trend-optimization-trading-strategy

RBI system
Research - papers, videos etc. 
Backtest - backtest, backtest 
Implement - into an algo 

ideas
- test different amounts of time for trending, ask luxee to build something that can look at data from the past and analyze how long each trend goes: 

where to go from here
1. figure out with the analyze_trend file how long do we tend trend for?
2. build out a backtest using the ideas derived from the above trending data 
    ex. if we tend to trend for 10 hours, and the market is bearish... and we see consolidation for 10 hours, maybe enter a short cause we know next trend may start soon
    ex. if the market is bullish, and we know that we tend to trend for 10 hours, then if there is an uptick of a new trend starting and its only the first hour, well we know the average trend goes for 10 hours, so maybe take that long and close before the 10 hours are up. 