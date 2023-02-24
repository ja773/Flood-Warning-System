from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem import flood
from floodsystem.station import MonitoringStation

def run():
    ''' Requirements for Task 2C '''
    stations = build_station_list()
    update_water_levels(stations)
    N = 10
    stats = flood.stations_highest_rel_level(stations, N)
    for i in stats:
        print(i.name + " " + str(MonitoringStation.relative_water_level(i)))
    return stats

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()