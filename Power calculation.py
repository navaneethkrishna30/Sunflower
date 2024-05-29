import pvlib as pv
from matplotlib import pyplot as plt
from pvlib import pvsystem
class DualAxisTrackerMount(pvsystem.AbstractMount):
    def get_orientation(self, solar_zenith, solar_azimuth):
        # no rotation limits, no backtracking
        return {'surface_tilt': solar_zenith, 'surface_azimuth': solar_azimuth}
        
#latitude and longitude for Hyderabad location
loc = location.Location(17.3, 78.4)

array = pvsystem.Array(
    #The previously defined dual-axis tracker.
    mount=DualAxisTrackerMount(),
    
    #Module parameters where pdc0 is the nominal power (1 kW), 
    module_parameters=dict(pdc0=1, gamma_pdc=-0.004, b=0.05),
    
    #is the temperature coefficient of power (-0.004 per degree Celsius), and b is a performance parameter.
    temperature_model_parameters=dict(a=-3.56, b=-0.075, deltaT=3))

#Defines a PV system that consists of the array defined above and an inverter with a nominal power of 3 kW.
system = pvsystem.PVSystem(arrays=[array], inverter_parameters=dict(pdc0=3))

#Creates a model chain object for the PV system at the given location. spectral_model='no_loss' specifies that no spectral losses are considered.
mc = pv.modelchain.ModelChain(system, loc, spectral_model='no_loss')

date = '2024-05-26'
times = pd.date_range(start=f'{date} 00:00:00', end=f'{date} 23:59:59', freq='1min', tz=timezone)

#Runs the PV system performance model using the clear sky weather data.
weather = loc.get_clearsky(times)
mc.run_model(weather)

mc.results.ac.plot()
plt.ylabel('Output Power')
plt.xlabel('Time')
plt.title('Hyderabad')
plt.show()
