"""This module contains a collection of functions related to analysis"""
import numpy as np
import matplotlib
def polyfit(dates, levels, p):
    '''takes waterlevel data over time, and returns a shifted polynomial that fits the data
    and the shift used. Useful to predict near fututre levels'''
    x = matplotlib.dates.date2num(dates)
    x = np.array(x)
    d0 = x[0]
    x = x-d0
    p_coeff = np.polyfit(x, levels, p)
    poly = np.poly1d(p_coeff)
    return poly, d0
