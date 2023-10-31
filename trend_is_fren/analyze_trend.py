# this file finds the time of trends, so the goal is to figure out how long do 
# we tend to trend for upward, down, or sideways then we can use this info 
# to build all types of backtests

import pandas as pd
import numpy as np

data = pd.read_csv('trend_is_fren/ETH-USD-15m-2021-1-02T00:00.csv')
data['datetime'] = pd.to_datetime(data['datetime'])

def calculate_trends(df):
    trends = []
    current_trend = None
    current_start = None

    for i in range(len(df)):
        if current_trend is None:  # Start of a new trend
            current_trend = 'Sideways'
            current_start = df['datetime'].iloc[i]
        elif df['close'].iloc[i] > df['close'].iloc[i-1]:  # Upward movement
            if current_trend != 'Upward':
                trends.append((current_trend, current_start, df['datetime'].iloc[i-1]))
                current_trend = 'Upward'
                current_start = df['datetime'].iloc[i]
        elif df['close'].iloc[i] < df['close'].iloc[i-1]:  # Downward movement
            if current_trend != 'Downward':
                trends.append((current_trend, current_start, df['datetime'].iloc[i-1]))
                current_trend = 'Downward'
                current_start = df['datetime'].iloc[i]
    
    # Append the last trend
    trends.append((current_trend, current_start, df['datetime'].iloc[-1]))

    return trends

trends = calculate_trends(data)

def calculate_duration(trend):
    start_time = trend[1]
    end_time = trend[2]
    duration = end_time - start_time
    duration_hours = duration.total_seconds() / 3600  # Convert duration to hours
    return duration_hours

upward_durations = []
downward_durations = []
sideways_durations = []

for trend in trends:
    duration = calculate_duration(trend)
    if trend[0] == 'Upward':
        upward_durations.append(duration)
    elif trend[0] == 'Downward':
        downward_durations.append(duration)
    else:
        sideways_durations.append(duration)

# Calculate average durations
avg_upward_duration = np.mean(upward_durations)
avg_downward_duration = np.mean(downward_durations)
avg_sideways_duration = np.mean(sideways_durations)

# Print the results
print("Average upward duration:", avg_upward_duration, "hours")
print("Average downward duration:", avg_downward_duration, "hours")
print("Average sideways duration:", avg_sideways_duration, "hours")