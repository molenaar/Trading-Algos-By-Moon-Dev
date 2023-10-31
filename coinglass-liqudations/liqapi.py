import requests
from datetime import datetime, timedelta

# Define the API endpoint for liquidation data
endpoint = "https://api.coinglass.com/v2/public/liquidations"

# Define the start time for the desired time periods
now = datetime.utcnow()

# Calculate the start times for different time periods
hour_ago = now - timedelta(hours=1)
four_hours_ago = now - timedelta(hours=4)
fourteen_hours_ago = now - timedelta(hours=14)
twentyfour_hours_ago = now - timedelta(hours=24)

# Define a function to retrieve liquidation data within a specific time range
def get_liquidations(start_time, end_time):
    start_timestamp = int(start_time.timestamp() * 1000)
    end_timestamp = int(end_time.timestamp() * 1000)
    
    # Send a GET request with the desired time range
    response = requests.get(endpoint, params={"start": start_timestamp, "end": end_timestamp})
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Error retrieving liquidation data:", response.text)
        return []

# Retrieve liquidation data for each time period
liquidations_in_past_hour = get_liquidations(hour_ago, now)
liquidations_in_4_hours = get_liquidations(four_hours_ago, now)
liquidations_in_14_hours = get_liquidations(fourteen_hours_ago, now)
liquidations_in_24_hours = get_liquidations(twentyfour_hours_ago, now)

# Print liquidation data for each time period
print("Liquidations in the past hour:")
print(liquidations_in_past_hour)
print("-----------")
print("Liquidations in the past 4 hours:")
print(liquidations_in_4_hours)
print("-----------")
print("Liquidations in the past 14 hours:")
print(liquidations_in_14_hours)
print("-----------")
print("Liquidations in the past 24 hours:")
print(liquidations_in_24_hours)
print("-----------")