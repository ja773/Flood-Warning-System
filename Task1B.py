from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    ''' Requirements for Task 1B'''
    stations = build_station_list()
    cambridge = 52.2053, 0.1218
    stationlist = stations_by_distance(stations, cambridge)
    tuplelist = []
    for i in stationlist[:10]:
        closestation = tuple([i[0].name, i[0].town, i[1]])
        tuplelist.append(closestation)

    for i in stationlist[-10:]:
        farstation = tuple([i[0].name, i[0].town, i[1]])
        tuplelist.append(farstation)
    print(tuplelist)
    return tuplelist

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()