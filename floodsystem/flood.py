'''This module contains a collection of functions related to flood analysis'''

import floodsystem.station
from floodsystem.utils import sorted_by_key

def stations_level_over_threshold(stations,tol):
    ''' Given a list of stations and a tolerance value,
     returns a list of tuples containing stations and the 
     latest relative water level over the tolerance '''
    
    inconsistents = floodsystem.station.inconsistent_typical_range_stations(stations)
    consistents = []
    overtols = []
    for i in stations:
        if i not in inconsistents:
            consistents.append(i)
    for i in consistents:
        if floodsystem.station.MonitoringStation.relative_water_level(i) > tol:
            tup = tuple(i,floodsystem.station.MonitoringStation.relative_water_level(i))
            overtols.append(tup)
    overtols = sorted_by_key(overtols,1)
    return overtols
    