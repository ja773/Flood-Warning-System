''' Unit test for the flood module '''

from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold

def test_flood_functions():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "1"
    coord = (-3.0, 4.0)
    trange = (0, 1)
    river = "River X"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s1.latest_level = 0.5

    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "2"
    coord = (-6.0, 8.0)
    trange = (0, 1)
    river = "River X"
    town = "My Town"
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s2.latest_level = 1

    s_id = "test-s-idz"
    m_id = "test-m-id"
    label = "3"
    coord = (-2.0, 4.0)
    trange = (0, 1)
    river = "River Y"
    town = "My Town"
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s3.latest_level = 2

    stations = [s1,s2,s3]

    assert stations_level_over_threshold(stations, 0.7) == [tuple([s3, 2]), tuple([s2, 1])]
    assert stations_highest_rel_level(stations, 2) == [s3,s2]