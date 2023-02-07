from floodsystem.stationdata import build_station_list
import floodsystem.geo as geo

def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()

    print(geo.rivers_by_station_number(stations, 9))


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    print()
    run()
