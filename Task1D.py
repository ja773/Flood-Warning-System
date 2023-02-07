from floodsystem.stationdata import build_station_list
import floodsystem.geo as geo

def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()

    # print the first 10 rivers with at least one monitoring station alphabetically
    print(sorted(list(geo.rivers_with_station(stations)))[:10])
    print()

    #print ordered lists of monitoring stations names for three example rivers
    print(sorted([i.name for i in geo.stations_by_river(stations)['River Aire']]))
    print()
    print(sorted([i.name for i in geo.stations_by_river(stations)['River Cam']]))
    print()
    print(sorted([i.name for i in geo.stations_by_river(stations)['River Thames']]))
    print()


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    print()
    run()
