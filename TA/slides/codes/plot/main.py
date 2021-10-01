import math

import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced numbers
x1 = np.linspace(0, 100, 1000)
x2 = np.linspace(0, 100, 1000)
x3 = np.linspace(0, 100, 1000)

# the function, which is y = x^2 here
y1 = x1**2
y2 = x2**3
y3 = np.exp(x3)

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x1, y1, 'r', label='n^2')
plt.plot(x2, y2, 'b', label='n^3')
# plt.plot(x3, y3, 'y', label='y=e^n')
# plt.plot(x3, x3*y3, 'black', label='y=ne^n')
plt.legend()

# show the plot
plt.show()