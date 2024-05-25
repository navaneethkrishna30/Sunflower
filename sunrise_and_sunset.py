from pvlib import solarposition, location
import pandas as pd

# Define the location (latitude and longitude)
latitude = 28.6  # Example latitude for New York City
longitude = 77.2  # Example longitude for New York City

# Define the date (in UTC)
date = pd.date_range(start='2024-05-11 00:00:00', end="2024-05-12", freq='D', tz='Asia/Kolkata')

# Create a Location object
loc = location.Location(latitude, longitude)

# Calculate sunrise, sunset, and transit times
sun_times = loc.get_sun_rise_set_transit(date)

print(sun_times['sunrise'])
print(sun_times['sunset'])