import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import floodsystem.plot as plot 
import floodsystem.flood as flood
import floodsystem.analysis as analysis
import numpy as np
from datetime import datetime, timedelta
import matplotlib
from matplotlib import pyplot as plt

def rel(level, typical):
    '''calculate relative level for hypothetical levels in the future'''
    rang = typical[1] - typical[0]
    level = level - typical[0]
    ratio = level/rang
    return ratio

def run():
    print("initialising")
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)


    print("running\n")
    for station in stations:
        if station.relative_water_level() is None:
            continue
        if station.relative_water_level() < 0.7:
            continue
        current_risk = False
        soon_risk = False
        worse = False
        worst = [0,0]
        dt = 3
        dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))
        if dates == [] or levels == []:
            continue
        poly, d0 = analysis.polyfit(dates, levels, 1)
        soon = np.polyval(poly,matplotlib.dates.date2num(datetime.today() + timedelta(5)))
        typ = station.typical_range
        if rel(levels[-1],typ) >= 1:
            current_risk = True
        worse = poly[1] > 0
        if rel(soon, typ) >= 1:
            soon_risk = True
                    
        if current_risk or soon_risk:
            plot.plot_water_level_with_fit(station, dates, levels, 1)
            print(station.name, end = ' ')
            if not soon_risk:
                if rel(levels[-1],typ) > 1.5:
                    print("is at a severe risk of imminent flooding, though levels may fall soon")
                elif rel(levels[-1],typ) > 1.1:
                    print("is at a high risk of imminent flooding, though levels are expected to fall soon")
                else:
                    print("is at a moderate risk of imminent flooding, though levels are expected to fall soon")
            elif soon_risk and current_risk and not worse:
                if rel(levels[-1],typ) > 1.5:
                    print("is at a severe risk of imminent flooding.")
                elif rel(levels[-1],typ) > 1.1:
                    print("is at a high risk of imminent flooding.")
                else:
                    print("is at a moderate risk of imminent flooding.")
            elif current_risk:
                if rel(levels[-1],typ) > 1.5:
                    print("is at a severe risk of imminent flooding, with conditions expected to worsen in the near future.")
                elif rel(levels[-1],typ) > 1.1:
                    print("is at a high risk of imminent flooding, with conditions expected to worsen in the near future.")
                else:
                    print("is at a moderate risk of imminent flooding, with conditions expected to worsen in the near future.")
            else:
                if (rel(worst[1],typ) > 3) and (worst[0]<=1):
                    print("is at a high risk of flooding in the near future.")
                elif (rel(worst[1],typ) > 2 and worst[1]<=1):
                    print("is at a moderate risk of flooding in the near future.")
                else:
                    print("is at a low risk of flooding in the near future.")

            print()
    print("done")

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
