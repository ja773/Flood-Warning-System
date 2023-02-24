from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem import flood

def run():
    ''' Requirements for Task 2B '''
    stations = build_station_list()
    update_water_levels(stations)
    tol = 0.8
    stats = flood.stations_level_over_threshold(stations,tol)
    for i in stats:
        print(i[0].name + " " + str(i[1]))
    return stats

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()
