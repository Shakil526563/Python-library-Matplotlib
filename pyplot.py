# -*- coding: utf-8 -*-
"""
Three line our complier able to draw
"""

import sys
import matplotlib
matplotlib.use("Agg")
"""An Anti-Grain Geometry (AGG) backend. """


import matplotlib.pyplot as plt
import numpy as np



x=np.array([0,5])
y=np.array([1,250])
plt.plot(x, y)
