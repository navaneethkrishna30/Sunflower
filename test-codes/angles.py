from pvlib import solarposition
import pandas as pd
import numpy as np

tz = 'Asia/Calcutta'
lat, lon = 17.4, 78.


times = pd.date_range(start='07-06-2024 05:29:00', end= "07-06-2024 18:54:00", freq="900s")

solpos = solarposition.get_solarposition(times, lat, lon)

#round off to nearest integer
azimuth_np_array = np.array(solpos['azimuth'].tolist())
azimuth_np_array = np.round(azimuth_np_array).astype(int)

elevation_np_array = np.array(solpos['elevation'].tolist())
elevation_np_array = np.round(elevation_np_array).astype(int)

print(elevation_np_array.tolist())
print(azimuth_np_array.tolist())