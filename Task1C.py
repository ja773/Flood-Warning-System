from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    ''' Requirements for Task 1C '''
    cambridge = (52.2053, 0.1218)
    stations = build_station_list()
    cambridgestations = stations_within_radius(stations, cambridge, 10)
    print(cambridgestations)
    return cambridgestations

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()


