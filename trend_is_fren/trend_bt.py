import backtesting
from backtesting import Backtest, Strategy
import pandas as pd
import numpy as np

# Define your custom strategy
class TrendFollowingStrategy(Strategy):

    def init(self):
        self.in_upward_trend = False
        self.upward_trend_start = None
        self.upward_trend_duration = None

    def next(self):
        if not self.in_upward_trend and self.data['close'] > self.data['close'].shift(1):
            self.in_upward_trend = True
            self.upward_trend_start = self.data.datetime.iloc[-1]
        elif self.in_upward_trend and self.data.datetime.iloc[-1] - self.upward_trend_start >= pd.Timedelta(hours=self.upward_trend_duration * 0.8):
            self.in_upward_trend = False
            self.sell()

        if not self.in_upward_trend and self.data['close'] < self.data['close'].shift(1):
            self.in_upward_trend = False

# Load and preprocess data
data = pd.read_csv('your_file.csv')
data['datetime'] = pd.to_datetime(data['datetime'])
data = data.set_index('datetime')

# Calculate average upward trend duration
trends = calculate_trends(data)
upward_durations = []

for trend in trends:
    if trend[0] == 'Upward':
        duration = calculate_duration(trend)
        upward_durations.append(duration)

avg_upward_duration = np.mean(upward_durations)

# Calculate the sell duration
sell_duration = avg_upward_duration * 0.8

# Configure the strategy with the average trend duration
bt = Backtest(data, TrendFollowingStrategy, cash=100000, commission=0)
bt.strategy.upward_trend_duration = avg_upward_duration

# Run the backtest
bt.run()

# Plot the backtest results
bt.plot()