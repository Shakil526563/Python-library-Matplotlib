# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 13:33:04 2022

@author: WIN10
"""

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")