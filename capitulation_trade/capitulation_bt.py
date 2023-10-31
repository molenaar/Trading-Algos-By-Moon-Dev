import backtesting
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import pandas as pd 

# Define your custom strategy
class VolumeSpikeStrategy(Strategy):

    def init(self):
        self.volume_spike_multiplier = self.params.volume_spike_multiplier
        self.set_commissions(lambda q, p: abs(q) * p * 0.0025)  # 0.25% trading fee
        self.capitulation_count = 0

    def next(self):
        if len(self.volume) > 30 and self.volume[-1] >= self.volume_spike_multiplier * self.volume[:-1].mean():
            self.capitulation_count += 1
            quantity = self.portfolio.cash * 0.25 / self.open
            self.buy(size=quantity)

# Backtest settings and data
data = backtesting.get_crypto_daily("ETH", start_date="2020-01-01", end_date="2021-01-01")

# Define the volume spike multiplier parameter and optimizer
params = dict(
    volume_spike_multiplier=range(1, 21)
)


data = pd.read_csv('/Users/tc/Dropbox/**HMV/*ATC/Weekly Code - ATC/ETH-USD-1h-2020-2-02T00:00.csv')
data.columns = [column.capitalize() for column in data.columns]
data = data.dropna()

bt = backtesting.Backtest(data, VolumeSpikeStrategy, cash=1000000, commission=.006)

#stats = bt.optimize(maximize='Equity Final [$]', timeperiod=range(20, 60, 5))
stats = bt.run()
print(stats)

bt.plot()