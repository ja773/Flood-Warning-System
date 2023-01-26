# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine


from floodsystem.utils import sorted_by_key  # noqa
#edited above line to "uitls" from ".utils". This broke tests, so I changed it back.


def rivers_with_station(stations):
    '''Takes a list of monitoring stations, and returns a set of the rivers
    monitored by those stations'''
    return set([i.river for i in stations])
    
def stations_by_river(stations):
    '''Takes a list of monitoring stations, and returns a dictionary mapping river names
    to their monitoring stations'''
    retval = {}
    for i in stations:
        if i.river in retval.keys():
            retval[i.river].append(i)
        else:
            retval[i.river] = [i]
    return retval

def rivers_by_station_number(stations, N):
    '''Takes a list of stations and an integer N, and returns a list of tuples
    (river_name, count) for the N rivers with the most monitoring stations in the list,
    in descending order of number of stations. If the Nth station in a draw, all the
    stations tied for Nth place are returned.'''
    
    counter = {}
    for i in stations:
        if i.river in counter.keys():
            counter[i.river] += 1
        else:
            counter[i.river] = 1
    flipped = sorted([(counter[i],i) for i in counter.keys()], reverse=True)
    retval = [(i,j) for (j,i) in flipped]
    while N < len(stations):
        if retval[N-1][1] == retval[N][1]:
            N+= 1
        else:
            break
    return retval[:N]

def stations_by_distance(stations, p):
    ''' Given a list of station objects and a coordinate p, 
    the function returns a list of (station, distance) tuples, 
    where distance (float) is the distance of the station (MonitoringStation) 
    from the coordinate p. '''

    dists = []
    for i in stations:
        dis = haversine(i.coord, p)
        dists.append(tuple([i,dis]))
    dists = sorted_by_key(dists, 1)
    return dists

def stations_within_radius(stations, centre, r):
    ''' This function returns a list of all stations (type MonitoringStation) 
    within radius r of a geographic coordinate x. '''

    stats = stations_by_distance(stations, centre)
    closest = []
    for i in stats:
        if i[1] <= r:
            closest.append(i[0].name)
    closest = sorted_by_key(closest, 0)
    return closest
