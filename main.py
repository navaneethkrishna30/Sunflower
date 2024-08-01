from pvlib import solarposition, location
from flask import Flask, request, jsonify
import pandas as pd
import numpy as np

app = Flask(__name__)


@app.route("/")
def hello_world():
    return f"API is up and running!"


@app.route("/sunrise_and_sunset", methods=["POST"])
def sunrise_and_sunset():
    data = request.get_json()
    
    # Retrieve data from the request
    latitude = float(data.get('latitude'))
    longitude = float(data.get('longitude'))
    date_str = data.get('date')
    timezone = data.get('timezone')

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
    
    return jsonify(response)


@app.route("/angles", methods=["POST"])
def angles():
    data = request.get_json()
    
    # Retrieve data from the request
    latitude = float(data.get('latitude'))
    longitude = float(data.get('longitude'))
    timezone = data.get('timezone')
    sunrise = data.get('sunrise')
    sunset = data.get('sunset')

    time_range = pd.date_range(start=sunrise, end=sunset, freq='900s', tz=timezone)

    sun_pos = solarposition.get_solarposition(time_range, latitude, longitude)

    #round off to nearest integer
    azimuth_np_array = np.array(sun_pos['azimuth'].tolist())
    azimuth_np_array = np.round(azimuth_np_array).astype(int)
    azimuth = azimuth_np_array.tolist()

    elevation_np_array = np.array(sun_pos['elevation'].tolist())
    elevation_np_array = np.round(elevation_np_array).astype(int)
    elevation = elevation_np_array.tolist()
    #response
    response = {
        'elevation': elevation,
        'azimuth': azimuth
    }

    return jsonify(response)


app.run(debug=True)