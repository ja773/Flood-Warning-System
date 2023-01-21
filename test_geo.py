"""Unit test for the geo module"""

from floodsystem.station import MonitoringStation
import floodsystem.geo as geo

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "1"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "2"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "3"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River Y"
    town = "My Town"
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert geo.rivers_with_station([s1,s2,s3]) == set(['River X', 'River Y'])
    assert geo.stations_by_river([s1,s2,s3]) == {'River X': [s1,s2], 'River Y':[s3]}
