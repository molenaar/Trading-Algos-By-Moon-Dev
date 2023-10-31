import backtesting
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import pandas as pd

# Define your custom strategy
class VolumeSpikeStrategy(Strategy):

    def init(self):
        self.volume_spike_multiplier = self.p.volume_spike_multiplier
        self.volume_spike = False
        self.enter_price = None

    def next(self):
        if self.volume[-1] >= self.volume_spike_multiplier * self.volume[:-1].mean() and self.enter_price is None:
            self.volume_spike = True
            self.enter_price = self.close[-1]
        elif self.volume_spike and self.close < self.enter_price:
            self.buy()

# Load and preprocess data
data = pd.read_csv('/Users/tc/Dropbox/**HMV/*ATC/Weekly Code - ATC/ETH-USD-1h-2020-2-02T00:00.csv')
data.columns = [column.capitalize() for column in data.columns]
data = data.dropna()

# Define parameters for optimization
parameters = dict(
    volume_spike_multiplier=range(1, 21)
)

# Run the optimization
bt = Backtest(data, VolumeSpikeStrategy, cash=1000000, commission=0.006)
stats = bt.optimize(parameters)

# Retrieve the best optimized parameters and run the backtest
best_params = stats["_strategy_params"].loc[0]
bt = Backtest(data, VolumeSpikeStrategy, cash=1000000, commission=0.006, volume_spike_multiplier=best_params.volume_spike_multiplier)
bt.run()

# Plot the backtest results
bt.plot()