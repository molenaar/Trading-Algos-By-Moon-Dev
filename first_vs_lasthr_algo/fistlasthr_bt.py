import pandas as pd
from backtesting import Backtest, Strategy

# Define your MorningClosingUpDownStrategy class here
class MorningClosingUpDownStrategy(Strategy):
    def init(self):
        self.morning_session = None  # Variable to track morning session performance
        
    def next(self):
        # Check if it's the morning session
        if self.data.index[-1].hour == 10 and self.data.index[-1].minute == 0:
            self.morning_session = self.data.Close[-1]  # Track the morning session close
        # Check if it's the closing session
        elif self.data.index[-1].hour == 16 and self.data.index[-1].minute == 0:
            # If morning session was up, assume closing session will be up
            if self.morning_session < self.data.Close[-1]:
                self.buy()
            # If morning session was down, assume closing session will be down
            elif self.morning_session > self.data.Close[-1]:
                self.sell()

# Load the data from the CSV file downloaded from Polygon.io
data = pd.read_csv('path_to_polygon_data.csv', parse_dates=['time'])
data.set_index('time', inplace=True)

# Subset the data for the morning and closing sessions
morning_data = data.between_time('10:00', '11:00')
closing_data = data.between_time('16:00', '17:00')

# Create an instance of the backtest with the strategy for Morning Session to Closing Session
bt1 = Backtest(morning_data, MorningClosingUpDownStrategy, cash=100000, commission=0.002)

# Run the backtest and get the results
results1 = bt1.run()

# Print the performance metrics for Morning Session to Closing Session
print(results1)

# Plot the performance for Morning Session to Closing Session
bt1.plot()

# Create a strategy for Morning Session to Afternoon Session
class MorningAfternoonDownStrategy(Strategy):
    def init(self):
        self.morning_session = None  # Variable to track morning session performance
        
    def next(self):
        # Check if it's the morning session
        if self.data.index[-1].hour == 10 and self.data.index[-1].minute == 0:
            self.morning_session = self.data.Close[-1]  # Track the morning session close
        # Check if it's the afternoon session
        elif self.data.index[-1].hour == 15 and self.data.index[-1].minute == 0:
            # If morning session was up, assume afternoon session will be down
            if self.morning_session < self.data.Close[-1]:
                self.sell()

# Create an instance of the backtest with the strategy for Morning Session to Afternoon Session
bt2 = Backtest(morning_data, MorningAfternoonDownStrategy, cash=100000, commission=0.002)

# Run the backtest and get the results
results2 = bt2.run()

# Print the performance metrics for Morning Session to Afternoon Session
print(results2)

# Plot the performance for Morning Session to Afternoon Session
bt2.plot()