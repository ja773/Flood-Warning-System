import datetime
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import floodsystem.plot as plot 
import floodsystem.flood as flood
def run():

    # Build list of stations
    stations = build_station_list()

    stations = flood.stations_highest_rel_level(stations, 5)

    dt = 2
    for i in range(5):
        dates, levels = fetch_measure_levels(stations[i].measure_id, dt=datetime.timedelta(days=dt))
        plot.plot_water_level_with_fit(stations[i], dates, levels,4)


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
