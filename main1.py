import matplotlib.pyplot as plt
import numpy as np

x = np.arry([1, 2, 3, 4])
y = x**2

# first plot whith x and Y data
plt.plot(x, y)

x1 = [2, 4, 6, 8]
y1 = [3, 5, 7, 9]

# second plot whith x1 and y1 data
plt.plot(x1, y1, '-.')

plt.xlable("X-axis data")
plt.ylabel("Y-axis data")
plt.titel('multiple plots')
plt.Show()