"""Unit test for the geo module"""

from floodsystem.station import MonitoringStation
import floodsystem.analysis as a
import numpy as np
from datetime import datetime, timedelta

def test_analysis_functions():
    x = [datetime(2017, 1, 1),datetime(2017, 1, 2),datetime(2017, 1, 3),datetime(2017, 1, 4),datetime(2017, 1, 5)]
    y = [2,4,14,38,82] # y = x^3 + x^2 + 2
    p, d0 = a.polyfit(x,y,3)
    assert np.polyval(np.poly1d([1,1,0,2]),10) == round(np.polyval(p, 10))
    assert d0 == 17167
