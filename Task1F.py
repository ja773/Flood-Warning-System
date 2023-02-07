from floodsystem.station import inconsistent_typical_range_stations
from floodsystem import stationdata

def run():
    ''' Requirements for Task 1F '''
    stations = stationdata.build_station_list()
    inconsists = inconsistent_typical_range_stations(stations)
    inconsistents = []
    for s in inconsists:
        inconsistents.append(s.name)
    inconsistents.sort()
    print(inconsistents)
    return inconsistents


if __name__ == "__main__":
    run()