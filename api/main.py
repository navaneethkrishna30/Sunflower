from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import pandas as pd
import numpy as np
import uvicorn
from pvlib import solarposition, location
from typing import List

app = FastAPI()


class SunriseSunsetRequest(BaseModel):
    latitude: float
    longitude: float
    date: str
    timezone: str


class AnglesRequest(BaseModel):
    latitude: float
    longitude: float
    timezone: str
    sunrise: str
    sunset: str


@app.get("/")
async def hello_world():
    return "API is up and running!"


@app.post("/sunrise_and_sunset")
async def sunrise_and_sunset(data: SunriseSunsetRequest):
    # Retrieve data from the request
    latitude = data.latitude
    longitude = data.longitude
    date_str = data.date
    timezone = data.timezone

    date = pd.date_range(start=date_str, end=date_str, freq='D', tz=timezone)

    # Create a Location object
    loc = location.Location(latitude, longitude)

    # Get sunrise and sunset times
    sun_times = loc.get_sun_rise_set_transit(date)

    # Prepare the response
    response = {
        'sunrise': sun_times['sunrise'].iloc[0].strftime('%Y-%m-%d %H:%M:%S'),
        'sunset': sun_times['sunset'].iloc[0].strftime('%Y-%m-%d %H:%M:%S')
    }

    return response


@app.post("/angles")
async def angles(data: AnglesRequest):
    # Retrieve data from the request
    latitude = data.latitude
    longitude = data.longitude
    timezone = data.timezone
    sunrise = data.sunrise
    sunset = data.sunset

    time_range = pd.date_range(start=sunrise, end=sunset, freq='900s', tz=timezone)

    sun_pos = solarposition.get_solarposition(time_range, latitude, longitude)

    # Round off to nearest integer
    azimuth_np_array = np.round(np.array(sun_pos['azimuth'].tolist())).astype(int)
    zenith_np_array = np.round(np.array(sun_pos['zenith'].tolist())).astype(int)
    
    azimuth = azimuth_np_array.tolist()
    zenith = zenith_np_array.tolist()
    
    # Response
    response = {
        'zenith': zenith,
        'azimuth': azimuth
    }

    return response