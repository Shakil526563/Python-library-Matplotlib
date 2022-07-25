# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 12:36:02 2022

@author: WIN10
"""

import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,5,8,6,9,7])
y=np.array([3,8,9,6,3,4])

plt.plot(x, y)
font={'family':'serif','color':'purple','size':'30'}
font1={'family':'serif','color':'red','size':'15'}
plt.title("tuition academic",font)
plt.xlabel("month",font1)
plt.ylabel('Money')
#plt.grid()
#plt.grid(axis='y')
#plt.grid(axis='x')
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
