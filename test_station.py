# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations


def test_station():

    # Create a station
   
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (3, 2)
    river = "River X"
    town = "My Town"
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = None
    river = "River X"
    town = "My Town"
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s1.station_id == s_id
    assert s1.measure_id == m_id
    assert s1.name == label
    assert s1.coord == coord
    assert s1.typical_range == trange
    assert s1.river == river
    assert s1.town == town
    assert inconsistent_typical_range_stations([s1, s2, s3]) == [s2, s3]
