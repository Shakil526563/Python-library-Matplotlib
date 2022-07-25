# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 13:15:31 2022

@author: WIN10
"""

import matplotlib.pyplot as plt
import numpy as np
a=np.array([1,5,8,9,6])
b=np.array([5,8,9,6,7])

plt.scatter(a,b)
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y,color='red',s=10)
"""plot x,y,color,s means size"""