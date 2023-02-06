from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key

def run():
    ''' Requirements for Task 1C '''
    cambridge = (52.2053, 0.1218)
    stations = build_station_list()
    cambridgestations = stations_within_radius(stations, cambridge, 10)
    stats = []
    for stat in cambridgestations:
        stats.append(stat.name)
    stats = sorted_by_key(stats, 0)
    print(stats)
    return stats

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()


