import pandas as pd
from backtesting import Backtest, Strategy

# Define your QQQBullBearStrategy class here
class QQQBullBearStrategy(Strategy):
    def init(self):
        self.is_bullish = None  # Variable to track the bullish/bearish sentiment
        self.first_hour_high = None  # Variable to track the high of the first hour
        self.first_hour_low = None  # Variable to track the low of the first hour
        self.qqq_data = None

    def on_backtest_start(self, start, end):
        # Load the QQQ data from Polygon.io
        self.qqq_data = pd.read_csv('path_to_polygon_qqq_data.csv', parse_dates=['time'])
        self.qqq_data.set_index('time', inplace=True)
        
        # Subset the QQQ data for the first hour of each day
        first_hour_data = self.qqq_data.groupby(self.qqq_data.index.date).head(1)
        
        # Calculate the high and low of the first hour
        self.first_hour_high = first_hour_data['high'].max()
        self.first_hour_low = first_hour_data['low'].min()

    def next(self):
        # Check if it's the first hour of the day
        if self.data.index[-1].hour == 9 and self.data.index[-1].minute == 30:
            # If the current price breaks above the first hour high, consider it bullish
            if self.data.Close[-1] > self.first_hour_high:
                self.is_bullish = True
            # If the current price breaks below the first hour low, consider it bearish
            elif self.data.Close[-1] < self.first_hour_low:
                self.is_bullish = False
            
        # Check if it's after the first hour and a sentiment has been determined
        elif self.data.index[-1].hour >= 10 and self.is_bullish is not None:
            if self.is_bullish:
                self.buy('BTC', self.data.Close[-1])  # Enter a long position in Bitcoin
            else:
                self.sell('BTC', self.data.Close[-1])  # Exit any existing Bitcoin position

# Load the QQQ data from the CSV file downloaded from Polygon.io
qqq_data = pd.read_csv('path_to_polygon_qqq_data.csv', parse_dates=['time'])
qqq_data.set_index('time', inplace=True)

# Load the Bitcoin data from the CSV file
btc_data = pd.read_csv('breakout_wick_algo/ETH-USD-15m-2018-1-02T00:00.csv', parse_dates=['timestamp'])
btc_data.set_index('timestamp', inplace=True)

# Create an instance of the backtest with the strategy
bt = Backtest(btc_data, QQQBullBearStrategy, cash=100000, commission=0.002)

# Run the backtest and get the results
results = bt.run()

# Print the performance metrics
print(results)

# Plot the performance
bt.plot()