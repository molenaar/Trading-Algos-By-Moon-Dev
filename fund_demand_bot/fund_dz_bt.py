from backtesting import Backtest, Strategy
import pandas as pd
# hide warnings
import warnings
warnings.filterwarnings('ignore')

class FundingRateStrategy(Strategy):
    funding_rate_threshold = -22
    short_funding_rate_threshold = 14  # New variable for shorting based on funding rate
    take_profit = 0.045
    max_loss = 0.05
    nothing = 1
    
    def init(self):
        self.buy_signal = self.I(lambda x: x < self.funding_rate_threshold, self.data['funding rate'])
        self.short_signal = self.I(lambda x: x > self.short_funding_rate_threshold, self.data['funding rate'])

    def next(self):
        price = self.data.Close[-1]
        tp_price_long = price * (1 + self.take_profit)
        sl_price_long = price * (1 - self.max_loss)
        
        tp_price_short = price * (1 - self.take_profit)
        sl_price_short = price * (1 + self.max_loss)

        # Long logic
        if self.buy_signal[-1] and not self.position:
            self.buy(sl=sl_price_long, tp=tp_price_long)
        # Short logic
        elif self.short_signal[-1] and not self.position:
            self.sell(sl=sl_price_short, tp=tp_price_short)


data = pd.read_csv('/Users/tc/Dropbox/dev/github/Trading-Algos-By-Moon-Dev/fund_demand_bot/1019funding_rate.csv')
data['Datetime'] = pd.to_datetime(data['datetime'], format='%m-%d-%y %H:%M:%S')

# Split the DataFrame based on the 'symbol' column and make a copy
#btc_data = data[(data['symbol'] == 'BTC-USD-dydx') | (data['symbol'] == 'BTC-USD')].copy()
btc_data = data[(data['symbol'] == 'ETH-USD-dydx') | (data['symbol'] == 'ETH-USD')].copy()

# make fake ohlc based off bid/ask
btc_data['Open'] = btc_data['ask']
btc_data['High'] = btc_data['ask']
btc_data['Low'] = btc_data['bid']
btc_data['Close'] = btc_data['ask']

btc_data.set_index('Datetime', inplace=True)

# Filter rows to keep only those occurring at 5-minute intervals
btc_data = btc_data[btc_data.index.minute % 1 == 0]

# Ensure the DataFrame is sorted by datetime (important for backtesting)
btc_data = btc_data.sort_values(by='Datetime')


bt = Backtest(btc_data, FundingRateStrategy, cash=1000000, commission=.006)

stats, heatmap = bt.optimize(
    funding_rate_threshold=range(-20, -40, -1),
    short_funding_rate_threshold=range(15, 35, 1),  # Optimization range for short threshold
    # take_profit=[i/100 for i in range(6, 15)],
    # max_loss=[i/100 for i in range(8,15)],
    nothing=[i/100 for i in range(1,3)],
    maximize='Equity Final [$]',
    return_heatmap=True)

print(stats)
print(heatmap.sort_values().iloc[-3:])
bt.plot()