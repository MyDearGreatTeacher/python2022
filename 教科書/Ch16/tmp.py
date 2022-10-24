import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([20, 10, 15, 18, 12])
y1 = np.array([20, 28, 30, 24, 34])
x2 = np.array([30, 18, 35, 40, 26, 24, 27])
y2 = np.array([30, 35, 25, 30, 42, 38, 35])
plt.plot(x1, y1, 'ro')
plt.plot(x2, y2, 'gx')
plt.plot(17, 32, 'b^')
plt.show()