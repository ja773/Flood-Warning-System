"""Unit test for the geo module"""

from floodsystem.station import MonitoringStation
import floodsystem.geo as geo

def test_geo_functions():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "1"
    coord = (-3.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "2"
    coord = (-6.0, 8.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    s_id = "test-s-idz"
    m_id = "test-m-id"
    label = "3"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River Y"
    town = "My Town"
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert geo.rivers_with_station([s1,s2,s3]) == set(['River X', 'River Y'])
    assert geo.stations_by_river([s1,s2,s3]) == {'River X': [s1,s2], 'River Y':[s3]}
    assert geo.rivers_by_station_number([s1,s2,s3], 4) == [('River X',2),('River Y',1)]
    assert geo.rivers_by_station_number([s1,s2,s3], 1) == [('River X',2)]
    assert geo.stations_by_distance([s1,s2], tuple([0.0,0.0])) == [(s1.name, 5.0), (s2.name, 10.0)]
    assert geo.stations_within_radius([s1,s2,s3],(0.0,0.0),6.0) == [s1.name, s3.name]