# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 13:34:46 2022

@author: WIN10
"""

import matplotlib.pyplot as plt
import numpy as np
a=np.array([2,5,8,9])
label=['green','red','blue','pink']

"""add labels"""
#plt.pie(a,labels=label)
myexplode = [0.5, 0, 0, 0]

plt.pie(a, labels = label, explode = myexplode, shadow = True)

"""To add a header to the legend, add the title parameter to the legend function."""
plt.legend(title="Four color")