'''This module contains a collection of functions related to flood analysis'''

import floodsystem.station
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import update_water_levels

def stations_level_over_threshold(stations,tol):
    ''' Given a list of stations and a tolerance value,
     returns a list of tuples containing stations and the 
     latest relative water level over the tolerance '''
    
    inconsistents = floodsystem.station.inconsistent_typical_range_stations(stations)
    consistents = []
    overtols = []
    for i in stations:
        if i not in inconsistents:
            if floodsystem.station.MonitoringStation.relative_water_level(i) is not None:
                consistents.append(i)
    for i in consistents:
        if floodsystem.station.MonitoringStation.relative_water_level(i) > tol:
            tup = tuple([i,floodsystem.station.MonitoringStation.relative_water_level(i)])
            overtols.append(tup)
    overtols = sorted_by_key(overtols,1, True)
    return overtols

def stations_highest_rel_level(stations, N):
    ''' Returns a list of the N stations (objects) 
    at which the water level, relative to the typical range, is highest. '''

    statslevels = []
    stats = []
    for i in stations:
        if floodsystem.station.MonitoringStation.relative_water_level(i) is not None:
            statslevels.append([i,floodsystem.station.MonitoringStation.relative_water_level(i)])
    statslevels = sorted_by_key(statslevels, 1, True)
    for i in range(N):
        stats.append(statslevels[i][0])
    return stats
