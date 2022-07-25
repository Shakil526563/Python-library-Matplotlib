# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 13:26:21 2022

@author: WIN10
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

#plt.bar(x,y,color='red',width=0.1)
plt.barh(x,y,height=0.1)
"""plot.barh ,here graph show horizontal"""