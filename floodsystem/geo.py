# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from utils import sorted_by_key  # noqa
#edited above line to "uitls" from ".utils"


def rivers_with_station(stations):
    '''Takes a list of monitoring stations, and returns a set of the rivers
    monitored by those stations'''
    return set([i.river for i in stations])
    
def stations_by_river(stations):
    '''Takes a list of monitoring stations, and returns a dictionary mapping river names
    to their monitoring stations'''
    retval = {}
    for i in stations:
        if i.river in retval.keys:
            retval[i.river].append(i)
        else:
            retval[i.river] = [i]
    return retval
