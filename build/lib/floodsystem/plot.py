"""This module contains a collection of functions related to plotting"""

from .utils import sorted_by_key  # noqa
from matplotlib import pyplot as plt
import matplotlib
from floodsystem.datafetcher import fetch_measure_levels
from datetime import datetime, timedelta
import numpy as np
import floodsystem.analysis as analysis

def plot_water_levels(station, dates, levels):
    '''Takes a station, dates, and the water levels at those dates. Plots the water level on
    a graph, and adds reference high and low water lines'''
    plt.plot(dates, levels,label = "Water Level")
    (low, high) = station.typical_range
    plt.plot([dates[0], dates[-1]],[low,low], label = "Typical low water")
    plt.plot([dates[0], dates[-1]],[high,high], label = "Typical high water")
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=90)
    plt.title(station.name)
    plt.tight_layout()
    plt.legend()
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    '''Takes a station, dates, and the water levels at those dates. Plots the water level on
    a graph, and adds reference high and low water lines. It also includes the best-fit
    polynomial.'''
    poly, d0 = analysis.polyfit(dates, levels, p)
    print(d0)
    x = matplotlib.dates.date2num(dates)
    plt.plot(dates, poly(x-d0), label = "Best Fit")
    plt.plot(dates, levels, '.', label = "Water Level")
    (low, high) = station.typical_range
    plt.plot([dates[0], dates[-1]],[low,low], label = "Typical low water")
    plt.plot([dates[0], dates[-1]],[high,high], label = "Typical high water")
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=90)
    plt.title(station.name)
    plt.tight_layout()
    plt.legend()
    plt.show()
