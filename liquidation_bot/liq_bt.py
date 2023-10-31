# backtest

import backtesting
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import pandas as pd 

# Define your custom strategy
class VolumeSpikeStrategy(Strategy):

    def init(self):
        self.volume_spike = False
        self.enter_price = None

    def next(self):
        if self.volume[-1] >= 10 * self.volume[:-1].mean() and self.enter_price is None:
            self.volume_spike = True
            self.enter_price = self.close[-1]
        elif self.volume_spike and self.close < self.enter_price:
            self.buy()

data = pd.read_csv('/Users/tc/Dropbox/**HMV/*ATC/Weekly Code - ATC/ETH-USD-1h-2020-2-02T00:00.csv')
data.columns = [column.capitalize() for column in data.columns]
data = data.dropna()

bt = backtesting.Backtest(data, VolumeSpikeStrategy, cash=1000000, commission=.006)

#stats = bt.optimize(maximize='Equity Final [$]', timeperiod=range(20, 60, 5))
stats = bt.run()
print(stats)

bt.plot()