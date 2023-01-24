from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    cambridge = 52.2053, 0.1218
    x = stations_by_distance(stations, cambridge)
    tuplelist = []
    for i in x[:10]:
        y = tuple([i[0], i[0].town, i[1]])
        tuplelist.append(y)

    for i in x[-10:]:
        y = tuple([i[0], i[0].town, i[1]])
        tuplelist.append(y)
    
    return tuplelist

if __name__ == "__main__":
    run()


