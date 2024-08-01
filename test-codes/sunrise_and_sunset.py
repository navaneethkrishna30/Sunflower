from pvlib import solarposition, location
import pandas as pd

latitude = 17.4
longitude = 78.4

# Define the date (in UTC)
date = pd.date_range(start='2024-06-07 00:00:00', end="2024-06-07 23:59:59", freq='D', tz='Asia/Kolkata')

# Create a Location object
loc = location.Location(latitude, longitude)

sun_times = loc.get_sun_rise_set_transit(date)

print(sun_times)
print(sun_times['sunrise'].iloc[0])
print(sun_times['sunset'].iloc[0])