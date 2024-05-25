from pvlib import solarposition
import pandas as pd

tz = 'Asia/Calcutta'
lat, lon = 28.6, 77.2


times = pd.date_range(start='11-05-2024', end= "11-05-2024")

print(times)

solpos = solarposition.get_solarposition(times, lat, lon)
print(solpos)